#Work backwards using a sorted dictionary to keep track of starting index and group length
#Note: the key idea is to use dictionary bisect Java -> treemap.floorkey()

from sortedcontainers import SortedDict
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr) : return m
        
        pos2length = SortedDict()
        
        #means starting from index 0, there is group length of n
        pos2length[0] = len(arr)
        
        #traverse the arr / break points backwards
        for i in range(len(arr) - 1, -1, -1):
            index = arr[i] - 1
            
            #this is equivalent to Java -> treemap.floorkey() function
            interval_index = pos2length.bisect_right(index) - 1
            floor, length = pos2length.popitem(index = interval_index)
            
            if floor != index:
                pos2length[floor] = index - floor
                if pos2length[floor] == m: return i
            if floor + length - 1 != index:
                pos2length[index + 1] = length - (index - floor) - 1
                if pos2length[index + 1] == m: return i
                
        return -1
