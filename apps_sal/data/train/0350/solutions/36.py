class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        if not A:
            return 0
        
        l = len(A)
        end = 0
        left1 = 0
        left2 = 0
        map1 = collections.defaultdict(int)
        map2 = collections.defaultdict(int)
        ans = 0
        
        while end < l:
            ch = A[end]
            
            map1[ch] += 1
            map2[ch] += 1
            
            while len(map1) > K and left1 < l:
                temp1 = A[left1]
                map1[temp1] -= 1
                if map1[temp1] == 0:
                    del map1[temp1]
                
                left1 += 1
                
            while len(map2) >= K and left2 < l:
                temp2 = A[left2]
                map2[temp2] -= 1
                if map2[temp2] == 0:
                    del map2[temp2]
                
                left2 += 1
            
            ans += left2 - left1
            end += 1
        
        return ans
