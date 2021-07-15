import bisect

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        cur, stack, idx, ans = 0, [0], [-1], float('inf')
        for i, x in enumerate(A):
            cur += x
            while len(stack) > 0 and stack[-1] >= cur:
                stack.pop()
                idx.pop()
            j = bisect.bisect_right(stack, cur - K)
            if j > 0:
                ans = min(ans, i - idx[j - 1])
            stack.append(cur)
            idx.append(i)
        
        if ans == float('inf'):
            return -1
        return ans
        

