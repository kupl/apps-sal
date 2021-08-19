def union(parent, rank, i, j):
    parI = find(parent, i)
    parJ = find(parent, j)
    if parI == parJ:
        return
    if rank[parI] < rank[parJ]:
        parent[parI] = parJ
    elif rank[parI] > rank[parJ]:
        parent[parJ] = parI
    else:
        parent[parJ] = parI
        rank[parI] += 1


def find(parent, i):
    if i != parent[i]:
        parent[i] = find(parent, parent[i])
    return parent[i]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        rank = [0] * n
        parent = list(range(n))
        factorToSet = {}
        for (i, num) in enumerate(A):
            for factor in range(2, int(math.sqrt(num) + 1)):
                if num % factor == 0:
                    if factor in factorToSet:
                        union(parent, rank, i, factorToSet[factor])
                    else:
                        factorToSet[factor] = i
                    cfactor = num // factor
                    if cfactor in factorToSet:
                        union(parent, rank, i, factorToSet[cfactor])
                    else:
                        factorToSet[cfactor] = i
            if num in factorToSet:
                union(parent, rank, i, factorToSet[num])
            else:
                factorToSet[num] = i
        for i in range(n):
            find(parent, i)
        return max(collections.Counter(parent).values())
