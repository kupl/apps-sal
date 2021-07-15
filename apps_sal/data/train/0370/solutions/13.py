class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def decompose(n):
            def rec(n, start):
                for i in range(start, int(math.sqrt(n)) + 1, 2):
                    if n % i == 0:
                        return rec(n // i, i) | {i}
                return {n}
            if n % 2 == 0:
                while n % 2 == 0:
                    n //= 2
                if n == 1:
                    return {2}
                return {2} | rec(n, 3)
            return rec(n, 3)
        prime_set = collections.defaultdict(list)
        for i in range(len(A)):
            for f in decompose(A[i]):
                prime_set[f].append(i)
        ls = list(range(len(A)))
        def find(x):
            if ls[x] != x:
                ls[x] = find(ls[x])
            return ls[x]
        def union(x, y):
            ls[find(x)] = find(y)
        for v in prime_set.values():
            for i in range(len(v) - 1):
                union(v[i], v[i+1])
        return max(Counter([find(i) for i in range(len(A))]).values())
