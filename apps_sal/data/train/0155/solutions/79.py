class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # stack, TC: O(N), SC: O(N).
        A, n = arr, len(arr)
        # stack is index with decreasing of values, pending jumpping from right, being popped when meet next wall on right.
        s, stack = [1] * (n + 1), []
        for i, x in enumerate(A + [float('inf')]):
            while stack and A[stack[-1]] < x:
                queue = [stack.pop()]
                while stack and A[stack[-1]] == A[queue[-1]]:
                    queue.append(stack.pop())
                # j is min between stack[-1] and i, reverse jump up to stack[-1] and i
                for j in queue:
                    if i - j <= d:
                        s[i] = max(s[i], s[j] + 1)
                    if stack and j - stack[-1] <= d:
                        s[stack[-1]] = max(s[stack[-1]], s[j] + 1)
            stack.append(i)
        return max(s[:-1])
