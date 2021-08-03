class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        queue = [[0, 0]]
        x = 0
        ans = float('inf')
        for index, val in enumerate(A):
            x += val
            while queue and x - queue[0][1] >= K:
                ans = min(ans, index + 1 - queue[0][0])
                queue.pop(0)
            while queue and x <= queue[-1][1]:
                queue.pop()
            queue.append([index + 1, x])
        if ans == float('inf'):
            return -1
        return ans
