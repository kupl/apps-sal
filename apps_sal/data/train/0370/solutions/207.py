class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        parent = {}
        size = defaultdict(lambda: 1)

        def ds(a):
            while a in parent:
                a = parent[a]
            return a

        def union(a, b):
            if (a := ds(a)) != (b := ds(b)):
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]

        for a in A:
            for d in factors(a):
                union(-d, a)

        return Counter(ds(a) for a in A).most_common(1)[0][1]


FS = {}


def factors(f):
    if (n := f) not in FS:
        if n & 1:
            FS[f] = factors3(f)
        else:
            n >>= 1
            while n & 1 == 0:
                n >>= 1
            if n > 1:
                FS[f] = factors3(n) + [2]
            else:
                FS[f] = [2]
    return FS[f]


def factors3(f, start=3):
    if (n := f) not in FS:
        for i in range(start, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                n = n // i
                while n % i == 0:
                    n = n // i
                if n > 1:
                    FS[f] = factors3(n, i + 2) + [i]
                else:
                    FS[f] = [i]
                break
        else:
            FS[f] = [f]
    return FS[f]
