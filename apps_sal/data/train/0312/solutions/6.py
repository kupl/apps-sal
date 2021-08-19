class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        profits = [0]
        for num in A:
            profits.append(profits[-1] + num)
        ans = float('inf')
        q = collections.deque()
        for i in range(len(profits)):
            py = profits[i]
            while q and py - profits[q[0]] >= K:
                ans = min(ans, i - q[0])
                q.popleft()
            while q and py - profits[q[-1]] <= 0:
                q.pop()
            q.append(i)
        return ans if ans != float('inf') else -1
