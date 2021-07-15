from functools import reduce
class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        parent = {}
        size = defaultdict(lambda: 1)

        def ds(a):
            return ds(parent[a]) if a in parent else a

        def union(a, b):
            if (a:=ds(a)) != (b:=ds(b)):
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
            return a

        F = defaultdict(set)
        for a in A:
            for d in factors(a):
                F[d].add(a)

        return max(size[reduce(union, fs)] for fs in list(F.values()))


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
          73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
          157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
          239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]
FS = {n: {n} for n in primes}
FS[1] = {}


def factors(f):
    if (n := f) not in FS:
        if n & 1:
            FS[f] = factors3(f)
        else:
            n >>= 1
            while n & 1 == 0:
                n >>= 1
            if n == 1:
                FS[f] = {2}
            else:
                FS[f] = {2} | factors3(n)

    return FS.get(f, set())


def factors3(f, start=3):
    if (n := f) not in FS:
        for i in range(start, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                n = n // i
                while n % i == 0:
                    n = n // i
                if n == 1:
                    FS[f] = {i}
                else:
                    FS[f] = {i} | factors3(n, i + 2)
                break
        else:
            FS[f] = {f}

    return FS[f]

