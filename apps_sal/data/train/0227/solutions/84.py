class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        K_original = K
        i = 0
        ans = 0
        curr = 0

        j = 0
        while(j < len(A)):
            if A[j] == 1 or K > 0:
                curr += 1
            else:
                curr = 0
            K -= 1 if (A[j] == 0 and K > 0) else 0
            j += 1
            ans = max(curr, ans)
            if K_original > 0 and K == 0:
                while(j < len(A) and A[j] == 1):
                    curr += 1
                    j += 1
                ans = max(curr, ans)
                while(i <= j and i < len(A) and K == 0):
                    if A[i] == 0:
                        K += 1
                    i += 1
                    curr -= 1
            # print(i,j,K, curr, ans)
        return ans
