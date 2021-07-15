import collections 


class Solution(object):
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        if not nums:
            return False
        
        if len(nums)%k != 0:
            return False
        
        count_map = collections.Counter(nums)
        
        while count_map:
            min_ele = min(count_map)
            
            for i in range(k):
                key_count = count_map.get(min_ele+i, None)
                if not key_count:
                    return False
                
                if key_count == 1:
                    del count_map[min_ele+i]
                else:
                    count_map[min_ele+i] -= 1
                    
        
        return True
