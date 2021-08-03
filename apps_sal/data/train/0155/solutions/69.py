
# 1340. Jump Game V

class Solution2:  # bottom-up dp
    # Time complexity O(NlogN + ND), where we are given D <= N
    # Space complexity O(N) for dp
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [1] * n
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            for di in [-1, 1]:
                for j in range(i + di, i + di + d * di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution:

    # All element are pushed in and poped from stack1&2 only once,
    # strick O(N) time. 复杂度严格符合O(N)。

    # Decreasing Stack + DP
    # Use a stack to keep the index of decreasing elements.
    # Iterate the array A. When we meet a bigger element a,
    # we pop out the all indices j from the top of stack,
    # where A[j] have the same value.

    # Then we update dp[i] and dp[stack[-1]].

    # Since all indices will be pushed and popped in stack,
    # appended and iterated in L once,
    # the whole complexity is guaranteed to be O(N).

    # All element are pushed in and poped from stack1&2 only once, strick O(N) time.
    # Time complexity O(N); Space complexity O(N)
    # Python runtime 120ms, beats 100%

    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [1] * (n + 1)
        stack = []
        for i, a in enumerate(arr + [float('inf')]):
            while stack and arr[stack[-1]] < a:
                L = [stack.pop()]
                while stack and arr[stack[-1]] == arr[L[0]]:
                    L.append(stack.pop())
                for j in L:
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    if stack and j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
            stack.append(i)
        return max(dp[:-1])


class Solution1:  # top-down dp
    # Time complexity O(ND)
    # Space complexity O(N) for dp
    def maxJumps(self, arr: List[int], d: int) -> int:

        n = len(arr)
        res = [0] * n

        def dp(i):
            if res[i]:
                return res[i]
            res[i] = 1
            for di in [-1, 1]:
                for j in range(i + di, i + di + d * di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    res[i] = max(res[i], dp(j) + 1)
            return res[i]

        return max(list(map(dp, list(range(n)))))

    # range(0, n) as input of dp func, then get the max of their results
