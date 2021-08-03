class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
        unions = collections.defaultdict(set)
        for i, n in enumerate(A):
            for p in primes:
                if p * p > n:
                    break
                while not n % p:
                    n //= p
                    unions[p].add(i)
            if n > 1:
                unions[n].add(i)
        ids = list(range(len(A)))

        def find(i):
            if ids[i] != i:
                ids[i] = find(ids[i])
            return ids[i]

        def union(l):
            s = set(find(i) for i in l)
            i = s.pop()
            while s:
                j = s.pop()
                ids[j] = i
        for l in list(unions.values()):
            union(l)
        c = collections.Counter(find(i) for i in range(len(A)))
        return max(c.values())
