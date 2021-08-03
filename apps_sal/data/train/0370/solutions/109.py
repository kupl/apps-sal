from collections import defaultdict
import math
from collections import deque


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, a):
        if self.parent[a] < 0:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.parent[root_a] <= self.parent[root_b]:
                self.parent[root_a] += self.parent[root_b]
                self.parent[root_b] = root_a
            else:
                self.parent[root_b] += self.parent[root_a]
                self.parent[root_a] = root_b

########################## Solution inspired by discussion O(n sqrt(max(A))) ################
# The main idea of this is to use prime factorization for each number in A which takes O(n sqrt(max(A))) and build a dictionary with the key of prime number and value of list of indices of A that have that prime factor. Then connect the indices in each list with union find.


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        def prime_factors(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return set([i]) | prime_factors(num // i)
            return set([num])

        uf = UnionFind(len(A))
        d = defaultdict(list)
        for i, a in enumerate(A):
            for p in prime_factors(a):
                d[p].append(i)

        for p, idx_list in list(d.items()):
            for i in range(len(idx_list) - 1):
                uf.union(idx_list[i], idx_list[i + 1])
        return -min(uf.parent)


########################### My O(n^2) solution which is TLE #############################
# class Solution:
    # def largestComponentSize(self, A: List[int]) -> int:
    #     uf = UnionFind(len(A))
    #     for i in range(len(A)-1):
    #         for j in range(i+1, len(A)):
    #             p1 = uf.find(i)
    #             p2 = uf.find(j)
    #             if p1 != p2 and math.gcd(A[i], A[j]) > 1:
    #                 uf.union(i, j)
    #     return -min(uf.parent)


########################### My simple bfs solution which is O(n^2) ##############################
# class Solution:
#     def largestComponentSize(self, A: List[int]) -> int:
#         max_so_far = 0
#         seen = [0]*len(A)
#         first_unseen = 0
#         while first_unseen is not None:
#             tmp = 0
#             seen[first_unseen] = 1
#             q = deque([(first_unseen, A[first_unseen])])
#             first_unseen = None
#             while q:
#                 idx, num1 = q.popleft()
#                 tmp += 1
#                 for i, a in enumerate(A):
#                     if not seen[i]:
#                         if math.gcd(a, num1) > 1:
#                             seen[i] = 1
#                             q.append((i, a))
#                         else:
#                             first_unseen = i
#             max_so_far = max(max_so_far, tmp)
#         return max_so_far
