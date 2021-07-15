class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def prime_factors(n):
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return prime_factors(n//i) | set([i])
            return set([n])
            # i = 2
            # while i ** 2 <= n:
            #     if n % i == 0:
            #         return prime_factors(n // i) | set([i])
            #     i += 1
            # return set([n])

        f = list(range(len(A)))

        def find(x):
            # if x not in f:
            #     f[x] = x
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        p2i = dict()
        for i, a in enumerate(A):
            primes = prime_factors(a)
            # print(i, primes)
            for p in primes:
                # if p not in p2i:
                #     p2i[p] = []
                # p2i[p].append(i)
                if p in p2i:
                    union(i, p2i[p])
                else:
                    p2i[p] = find(i)
        # for indexes in p2i.values():
        #     for i in range(len(indexes) - 1):
        #         union(indexes[i], indexes[i + 1])
        # print(p2i)
        # print(list(map(find, range(len(A)))))
        counts = Counter(map(find, range(len(A))))
        return counts.most_common(1)[0][1]
