from collections import defaultdict
from math import sqrt


class DSU(object):
    def __init__(self, n):
        self.ds = list(range(n))

    def find(self, v):
        if self.ds[v] != v:
            self.ds[v] = self.find(self.ds[v])
        return self.ds[v]

    def union(self, p1, p2):
        pp1, pp2 = self.find(p1), self.find(p2)
        self.ds[pp1] = pp2


class Solution(object):
    def uniqPrime(self, n):
        l = []
        while n % 2 == 0:
            l.append(2)
            n = n // 2

        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                l.append(i)
                n = n // i
        if n > 2:
            l.append(n)

        return list(set(l))

    def largestComponentSize(self, A):
        primes = defaultdict(list)
        n = len(A)
        for i in range(n):
            p = self.uniqPrime(A[i])
            for x in p:
                primes[x].append(i)

        # now we need to merge the disjoint sets and see which is the longest
        uf = DSU(n)
        for i in list(primes.items()):
            vals = i[1]
            for j in range(len(vals) - 1):
                uf.union(vals[j], vals[j + 1])

        return max(Counter([uf.find(i) for i in range(n)]).values())
# class Dis_set_node:
#     def __init__(self):
#         self.parent = None
#         self.size = 1

# class Dis_set:
#     def __init__(self):
#         self.forest = {}

#     def addSet(self, node, key):
#         self.forest[key] = node

#     def find(self, p):
#         while self.forest[p].parent is not None:
#             self.forest[p].parent = self.forest[self.forest[p].parent].parent
#             p = self.forest[p].parent

#         return p

#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)

#         if x != y:
#             if self.forest[x].size < self.forest[y].size:
#                 x, y = y, x

#             self.forest[y].parent = x
#             self.forest[x].size += self.forest[y].size


# class Solution:
#     def largestComponentSize(self, A: List[int]) -> int:
#         prime_factors = {key:value for key, value in zip([n for n in A], [[] for _ in range(len(A))])}

#         up_to = max(A)

#         primes = set()
#         comps = set()

#         for i in range(2, up_to + 1):
#             if i not in comps:
#                 primes.add(i)
#                 comp = i * 2

#                 if i in prime_factors:
#                         prime_factors[i].append(i)

#                 while comp <= up_to:
#                     comps.add(comp)

#                     if comp in prime_factors:
#                         prime_factors[comp].append(i)

#                     comps.add(comp)
#                     comp += i

#         djus = Dis_set()

#         for p in primes:
#             djus.addSet(Dis_set_node(), p)

#         for pf in prime_factors.values():
#             if not pf:
#                 continue

#             for p1, p2 in zip(pf, pf[1:]):
#                 djus.forest[djus.find(p1)].size += 1
#                 djus.union(p1, p2)


#         print([node.size for node in djus.forest.values()])

        # print(self.prime_factors)

#         groups = []

#         for n in A:
#             i = 0
#             to_merge = []

#             while i < len(groups):
#                 if groups[i][0] & (self.prime_factors[n]):
#                     to_merge.append(groups.pop(i))
#                 else:
#                     i += 1

#             to_add = [self.prime_factors[n], 1]


#             for merge in to_merge:
#                 to_add = [merge[0] | to_add[0], merge[1] + to_add[1]]


#             groups.append(to_add)


#         return max(groups, key=lambda x:x[1])[1]


#     def seive(self, up_to):
#         primes = set()
#         comps = set()

#         for i in range(2, up_to + 1):
#             if i not in comps:
#                 primes.add(i)
#                 comp = i * 2

#                 if i in self.prime_factors:
#                         self.prime_factors[i].add(i)

#                 while comp <= up_to:
#                     comps.add(comp)

#                     if comp in self.prime_factors:
#                         self.prime_factors[comp].add(i)

#                     comps.add(comp)
#                     comp += i

#         return primes
