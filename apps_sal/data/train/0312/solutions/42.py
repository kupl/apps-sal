class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        pre = [0]
        n = len(A)
        for num in A:
            pre.append(num + pre[-1])

        ans = n + 1
        stack = deque()
        for i in range(n + 1):
            while stack and pre[i] - pre[stack[0]] >= K:
                ans = min(ans, i - stack.popleft())

            while stack and pre[i] <= pre[stack[-1]]:
                stack.pop()
            stack.append(i)

        return ans if ans <= n else -1
