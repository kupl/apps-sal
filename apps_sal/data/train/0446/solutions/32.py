class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        dic, a = {}, []
        for x in arr:
            dic[x] = dic.get(x, 0) + 1
        for x in dic:
            a.append(dic[x])
        a.sort(reverse = True)
        while a:
            x = a.pop()
            if x > k:
                return len(a) + 1
            k -= x
        return 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dic, count = {}, []
#         for x in arr:
#             dic[x] = dic.get(x,0)+1
        
#         for x in dic:
#             count.append(dic[x])
#         count.sort(reverse = True)
#         while k > 0 and count:
#             if k - count[-1] >= 0:
#                 k -= count[-1]
#                 count.pop()
#             else:
#                 k -= count[-1]

#         return(len(count))
                
                

