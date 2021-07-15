class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i, ans = 0, 0
        for j, num in enumerate(A):
            if num == 0:
                K -= 1
            while K < 0:
                if A[i] == 0:
                    K += 1
                i += 1
            ans = max(ans, j-i+1)
        return ans
        
        ans = 0
        start, end = 0, 0
        
        while end < len(A):
            if A[end] == 1:
                ans = max(ans, end-start+1)
                end+=1
            else:
                if K != 0:
                    ans = max(ans, end-start+1)
                    end+=1
                    K -= 1
                else:
                    if A[start] == 0:
                        K+=1
                    start+=1
        return ans

