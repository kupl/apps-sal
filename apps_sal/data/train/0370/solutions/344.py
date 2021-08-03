class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = {}
        size = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(rootlist):
            if not rootlist:
                return
            for i in range(1, len(rootlist)):
                parent[rootlist[i]] = rootlist[0]
                size[rootlist[0]] += size[rootlist[i]]
            size[rootlist[0]] += 1
        fact = [[] for _ in range(len(A))]
        for j in range(len(A)):
            num, p = A[j], 2
            while num >= p * p:
                if num % p == 0:
                    fact[j].append(p)
                    size[p], parent[p] = 0, p
                    while num % p == 0:
                        num //= p
                p += 1
            if num > 1:
                fact[j].append(num)
                size[num], parent[num] = 0, num
        for i in range(len(fact)):
            rootset = set()
            for factor in fact[i]:
                rootset.add(find(factor))
            union(list(rootset))
        return max(size.values())
