from typing import Deque, Dict, List, Set, Tuple
'\n952. Largest Component Size by Common Factor.  Hard\n\nGiven a non-empty array of unique positive integers A,\nconsider the following graph:\n\nThere are A.length nodes, labelled A[0] to A[A.length - 1];\nThere is an edge between A[i] and A[j] if and only if\nA[i] and A[j] share a common factor greater than 1.\nReturn the size of the largest connected component in the graph.\n\nExample 1:\nInput: [4,6,15,35]\nOutput: 4\n\nExample 2:\nInput: [20,50,9,63]\nOutput: 2\n\nExample 3:\nInput: [2,3,6,7,4,12,21,39]\nOutput: 8\n\nNote:\n1 <= A.length <= 20000\n1 <= A[i] <= 100000\n\nAccepted 18,093 / 53,552 submissions.\n'


def gen_primes():
    """
    Prime number generator, optimized to try only odd numbers.
    How to populate a list with some range of generated values:
        list(itertools.islice((p for p in gen_primes_opt()), beg_num, end_num)))
    """
    yield 2
    prime_divs = collections.defaultdict(list)
    candidate = 3
    while True:
        if candidate in prime_divs:
            for prime_div in prime_divs[candidate]:
                prime_divs[prime_div * 2 + candidate].append(prime_div)
            del prime_divs[candidate]
        else:
            yield candidate
            prime_divs[candidate * candidate] = [candidate]
        candidate += 2


class Solution:

    def prime_fac_set(self, num: int):
        pfs = set()
        for prime in self.primes:
            if num % prime == 0:
                pfs.add(prime)
            if prime >= num:
                break
        return pfs

    def largestComponentSizeWip(self, A: List[int]) -> int:
        return 0
        pcomps = collections.defaultdict(set)
        edges = collections.defaultdict(set)
        for num in A:
            pfs = self.prime_fac_set(num)
            prv = None
            for prime in pfs:
                pcomps[prime].add(num)
                if prv is None:
                    prv = prime
                else:
                    edges[prv].add(prime)
                    prv = prime
        max_size = 0
        print(edges)
        for (prm, num_set) in list(pcomps.items()):
            the_set = num_set
            the_prm = prm
            while the_prm in edges:
                the_set.update(edges[the_prm])
            max_size = max(max_size, len(the_set))
        return max_size

    def largestComponentSize(self, A: List[int]) -> int:
        """
        Step 1: get primes less than sqrt(max(A))
        Step 2: compute factors for each number in A
        Step 3: use union-find to link two primes
                if they are factors of the same number in A
        Step 4: for each number in A, add to its union
                (the union represented by its smallest prime)

        Runtime: 1068 ms, faster than 97.39% of Python3 online submissions for Largest Component Size by Common Factor.
        Memory Usage: 19 MB, less than 71.90% of Python3 online submissions for Largest Component Size by Common Factor.
        """
        primes = []
        for x in range(2, int(max(A) ** 0.5) + 1):
            for y in primes:
                if x % y == 0:
                    break
            else:
                primes.append(x)
        factors = collections.defaultdict(list)
        for a in A:
            x = a
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    factors[a].append(p)
                    while x % p == 0:
                        x //= p
            if x > 1:
                factors[a].append(x)
                primes.append(x)
        n = len(primes)
        p2i = {p: i for (i, p) in enumerate(primes)}
        parent = [i for i in range(n)]

        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            (pi, pj) = (find(i), find(j))
            if pi != pj:
                parent[pi] = pj
        for a in A:
            if factors[a]:
                p0 = factors[a][0]
                for p in factors[a][1:]:
                    union(p2i[p0], p2i[p])
        count = collections.Counter((find(p2i[factors[a][0]]) for a in A if factors[a]))
        return max(count.values())
