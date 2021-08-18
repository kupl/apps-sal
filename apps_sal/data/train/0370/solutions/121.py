class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        record = [-1] * n
        primes = collections.defaultdict(list)

        def get_primes(i):
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    return get_primes(i // j) | set([j])
            return set([i])

            return res

        def find(a):
            if record[a] < 0:
                return a
            record[a] = find(record[a])
            return record[a]

        def union(i, j):
            a, b = find(i), find(j)
            if a != b:
                if a < b:
                    record[a] = b
                else:
                    record[b] = a

        for i, v in enumerate(A):
            primes_set = get_primes(v)
            for j in primes_set:
                primes[j].append(i)

        for _, indexes in list(primes.items()):
            for i in range(len(indexes)):
                union(indexes[0], indexes[i])

        res = 0
        mapping = collections.defaultdict(set)
        for i in range(n):
            root = find(i)
            mapping[root].add(i)
            if len(mapping[root]) > res:
                res = len(mapping[root])
        return res
