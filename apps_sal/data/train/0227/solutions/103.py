class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right = 0, 0
        n, c1, c0 = len(A), 0, 0
        ans = 0
        while True:
            if c0 <= K:
                ans = max(ans, right - left)
                if right < n:
                    right += 1
                    x = A[right - 1]
                    if x:
                        c1 += 1
                    else:
                        c0 += 1
                else:
                    return ans
            else:
                x = A[left]
                left += 1
                if x:
                    c1 -= 1
                else:
                    c0 -= 1
