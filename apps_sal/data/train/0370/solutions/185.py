class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr


class Solution:
    def primes_set(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.primes_set(n // i) | set([i])
        return set([n])

    def largestComponentSize(self, A):
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set:
                primes[q].append(i)

        for _, indexes in list(primes.items()):
            for i in range(len(indexes) - 1):
                UF.union(indexes[i], indexes[i + 1])

        return max(Counter([UF.find(i) for i in range(n)]).values())

# class Solution:
#     def largestComponentSize(self, A: List[int]) -> int:
#         graph = {}
#         for i in range(0, len(A)):
#             for j in range(i+1, len(A)):
#                 if self.check(A[i], A[j]):
#                     if A[i] not in graph:
#                         graph[A[i]] = [A[j]]
#                     else:
#                         graph[A[i]].append(A[j])
#                     if A[j] not in graph:
#                         graph[A[j]] = [A[i]]
#                     else:
#                         graph[A[j]].append(A[i])
#         self.visited = set()
#         self.total = 0
#         for node in graph:
#             self.visited.add(node)
#             self.traverse(node, graph, 0)
#         return self.total

#     def traverse(self, root, graph, count):
#         # if root in self.visited:
#         #     self.total = max(self.total, count)
#         #     return
#         # self.visited.add(root)
#         # for neigh in graph[root]:
#         #     self.traverse(neigh, graph, count + 1)
#         queue = [root]
#         while queue:
#             current = queue.pop(0)
#             count += 1
#             for neigh in graph[current]:
#                 if neigh not in self.visited:
#                     self.visited.add(neigh)
#                     queue.append(neigh)
#         self.total = max(self.total, count)
#         return


#     def check(self, num1, num2):
#         i = 2
#         while i <= num1:
#             if num2 % i == 0 and num1 % i == 0:
#                 return True
#             i += 1
#         return False
