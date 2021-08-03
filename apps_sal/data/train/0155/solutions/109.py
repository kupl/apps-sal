import functools


class Solution:
    def maxJumps(self, A, d):
        N = len(A)
        graph = collections.defaultdict(list)

        def jump(iterator):
            stack = []
            for i in iterator:
                while stack and A[stack[-1]] < A[i]:
                    j = stack.pop()
                    if abs(i - j) <= d:
                        graph[j].append(i)
                stack.append(i)

        jump(range(N))
        jump(reversed(range(N)))

        @functools.lru_cache(maxsize=None)
        def height(i):
            return 1 + max(map(height, graph[i]), default=0)

        return max(map(height, range(N)))
