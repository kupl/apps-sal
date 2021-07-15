from collections import Counter
from functools import lru_cache
import math

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        # Backtracking
        # Time  complexity: O(N^N)
        # Space complexity: O(N)
        # N = len(A)
        # count = Counter(A)

        # graph = {x: [] for x in count}
        # for x in count:
        #     for y in count:
        #         if int((x + y) ** .5 + 0.5) ** 2 == x + y:
        #             graph[x].append(y)

        # def dfs(x, todo):
        #     count[x] -= 1
        #     if todo == 0:
        #         ans = 1
        #     else:
        #         ans = 0
        #         for y in graph[x]:
        #             if count[y]:
        #                 ans += dfs(y, todo - 1)

        #     count[x] += 1
        #     return ans

        # return sum(dfs(x, len(A) - 1) for x in count)


        # Dynamic Programming
        # Time  complexity: O(N^2 x 2^N) = O(sum_{k=1}^{N} C_N^K x C_k^2)
        # Space complexity: O(N x 2^N)
        N = len(A)

        def edge(x, y):
            r = math.sqrt(x + y)
            return int(r + 0.5) ** 2 == x + y

        graph = [[] for _ in range(len(A))]
        for i, x in enumerate(A):
            for j in range(i):
                if edge(x, A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        # find num of hamiltonian paths in graph
        @lru_cache(None)
        def dfs(node, visited):
            if visited == (1 << N) - 1:
                return 1

            ans = 0
            for nei in graph[node]:
                if (visited >> nei) & 1 == 0:
                    ans += dfs(nei, visited | 1 << nei)
            return ans

        ans = sum(dfs(i, 1 << i) for i in range(N))
        count = Counter(A)
        for v in list(count.values()):
            ans //= math.factorial(v)
        return ans


        # c = Counter(A)
        # cand = {i: {j for j in c if int((i+j)**.5) ** 2 == i + j} for i in c}
        # self.res = 0

        # def dfs(x, left=len(A)-1):
        #     c[x] -= 1
        #     if left == 0:
        #         self.res += 1
        #     for y in cand[x]:
        #         if c[y]:
        #             dfs(y, left - 1)
        #     c[x] += 1

        # for x in c: dfs(x)
        # return self.res


        # def backtrack(i, A):
        #     if i > 1:
        #         val = A[i - 2] + A[i - 1]
        #         is_square = math.sqrt(val) == math.floor(math.sqrt(val))
        #         if not is_square:
        #             return

        #     if i == len(A):
        #         output.append(A)
        #         return

        #     for j in range(i, len(A)):
        #         A[i], A[j] = A[j], A[i]
        #         search = (i, A[i], tuple(A[:i]))
        #         if search not in seen:
        #             seen.add(search)
        #             backtrack(i + 1, A)

        #         A[i], A[j] = A[j], A[i]

        # output, seen = [], set()
        # backtrack(0, A)
        # return len(output)


