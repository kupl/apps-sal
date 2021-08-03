class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # c1 and c0 are the count of 1 and 0 between left and right
        left, right = 0, 0
        n, c1, c0 = len(A), 0, 0
        ans = 0
        while True:
            if c0 <= K:
                # it is a legal interval
                ans = max(ans, right - left)
                # move right
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
                # move left
                x = A[left]
                left += 1
                if x:
                    c1 -= 1
                else:
                    c0 -= 1
