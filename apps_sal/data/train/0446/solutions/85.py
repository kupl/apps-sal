class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        
        for i in range(len(arr)):
            if(arr[i] in dic):
                dic[arr[i]] += 1
            else:
                dic[arr[i]] = 1
                
        dic = {k: v for k, v in sorted(list(dic.items()), key=lambda item: item[1])}
        
        for i in dic:
            if(k > 0):
                if(k > dic[i]):
                    k -= dic[i]
                    dic[i] = 0
                else:
                    dic[i] -= k
                    k = 0
            else:
                break
         
        ans = 0
        
        for i in dic:
            if(dic[i]>0):
                ans += 1
                
        return ans

