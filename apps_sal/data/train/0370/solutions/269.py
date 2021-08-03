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
#         # go through A,
#         # try each element from each group
#         ## if divides on element - accumulate groups, combine groups, add to group
#         ## else create new group
#         groups = []
#         for n in A:
#             indexesOfGroups = []
#             added = False
#             for i, g in enumerate(groups):
#                 for e in g:
#                     g = gcd(n, e)
#                     if g > 1:
#                         indexesOfGroups.append(i)
#                         added = True
#                         break
#             if not added:
#                 groups.append([n])
#                 continue
#             if indexesOfGroups:
#                 mainGrIdx = indexesOfGroups[0]
#                 mainGr = groups[mainGrIdx]
#                 for i in range(len(indexesOfGroups)-1, 0, -1):
#                     idx = indexesOfGroups[i]
#                     mainGr.extend(groups[idx])
#                     del groups[idx]
#                 mainGr.append(n)
#         # print(groups)

#         mx = 0
#         for g in groups:
#             mx = max(mx, len(g))
#         return mx
