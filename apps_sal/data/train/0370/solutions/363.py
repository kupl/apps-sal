# all primes less than sqrt(100000)
primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
]


def prime_factors(n: int) -> List[int]:
    if n == 1:
        return []
    for p in primes:
        if n % p == 0:
            return [p] + prime_factors(n // p)
    return [n]


def group_by_factors(A):
    groups = defaultdict(set)
    for a in A:
        for p in prime_factors(a):
            groups[p].add(a)
    return list(groups.values())


# TODO: this uses up about 2/3 of the runtime by itself
def adjacencies_by_intersection(gs):
    adj = [[] for _ in range(len(gs))]
    for x in range(len(gs)):
        for y in range(x):
            if gs[x] & gs[y]:
                adj[x].append(y)
                adj[y].append(x)
    return adj


def bfs(gs, adj, target):
    unvisited = set(range(len(gs)))
    largest = 0
    while unvisited:
        v = unvisited.pop()
        q = [v]

        group = set()
        while q:
            n = q.pop()
            group.add(n)
            for x in adj[n]:
                if x in unvisited:
                    unvisited.remove(x)
                    q.append(x)
        largest = max(largest, len(set(n for i in group for n in gs[i])))
        # try to short circuit
        if largest >= target:
            return largest
    return largest


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # group by prime factors and filter out singletons
        gs = [g for g in group_by_factors(A) if len(g) > 1]

        # build adjacency relations
        adj = adjacencies_by_intersection(gs)

        # bfs
        target = len(A) // 2
        return bfs(gs, adj, target)

