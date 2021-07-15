class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        size = 0
        adict = {}
        for item in arr:
            if item not in adict:
                adict[item] = 1
                size += 1
            else: 
                adict[item] += 1
        
        sort = sorted(adict.items(), key=lambda x: x[1])
        
        for i in sort:
            #print(i[1])
            if k >= i[1]:
                #print(i[1])
                k -= i[1]
                size -= 1
                #print(k)
                #print(size)
        
        return size
