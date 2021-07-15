from typing import Deque, Dict, List, Set, Tuple
'''
952. Largest Component Size by Common Factor.  Hard

Given a non-empty array of unique positive integers A,
consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if
A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

Example 1:
Input: [4,6,15,35]
Output: 4

Example 2:
Input: [20,50,9,63]
Output: 2

Example 3:
Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:
1 <= A.length <= 20000
1 <= A[i] <= 100000

Accepted 18,093 / 53,552 submissions.
'''


def gen_primes():
    '''
    Prime number generator, optimized to try only odd numbers.
    How to populate a list with some range of generated values:
        list(itertools.islice((p for p in gen_primes_opt()), beg_num, end_num)))
    '''
    yield 2                                     # return the first prime number
    prime_divs = collections.defaultdict(list)  # map numbers to their prime divisors
    candidate = 3
    while True:
        if candidate in prime_divs:
            for prime_div in prime_divs[candidate]:
                prime_divs[prime_div*2 + candidate].append(prime_div)
            del prime_divs[candidate]           # sieve no longer needed for candidate
        else:
            yield candidate                     # yield the next prime number
            prime_divs[candidate * candidate] = [candidate] # start sieve for sqaure
        candidate += 2



class Solution:

    def __init__(self):
        self.prime_gen = gen_primes()
        self.primes = [next(self.prime_gen) for _ in range(55)]


    def get_primes(self, lower_bound: int) -> List[int]:
        while self.primes[-1] < lower_bound:
            self.primes.append(next(self.prime_gen))
        return self.primes

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
        for prm, num_set in list(pcomps.items()):
            the_set = num_set
            the_prm = prm
            while the_prm in edges:
                the_set.update(edges[the_prm])
            max_size = max(max_size, len(the_set))


        return max_size



    def largestComponentSize(self, A: List[int]) -> int:
        '''
        Step 1: get primes less than sqrt(max(A))
        Step 2: compute factors for each number in A
        Step 3: use union-find to link two primes
                if they are factors of the same number in A
        Step 4: for each number in A, add to its union
                (the union represented by its smallest prime)
                
        Runtime: 1000 ms, faster than 99.35% of Python3 online submissions for Largest Component Size by Common Factor.
        Memory Usage: 19.4 MB, less than 55.56% of Python3 online submissions for Largest Component Size by Common Factor.
        '''
        # primes = []
        # for x in range(2, int(max(A)**0.5)+1):
        #     for y in primes:
        #         if x % y == 0:
        #             break
        #     else:
        #         primes.append(x)

        lowerb = int(max(A)**0.5) + 1
        primes = self.get_primes(lowerb)

        factors = collections.defaultdict(list)         # compute factors of each 'a'
        for a in A:
            x = a
            for p in primes:
                if p*p > x:
                    break
                if x % p == 0:
                    factors[a].append(p)
                    while x % p == 0:
                        x //= p
            if x > 1:                                   # a new prime found
                factors[a].append(x)
                primes.append(x)

        primes = list(set(primes))
        n = len(primes)
        p2i = {p: i for i,p in enumerate(primes)}       # prime to index

        parent = [i for i in range(n)]                  # union-find on primes

        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i,j):
            pi, pj = find(i), find(j)
            if pi != pj:
                parent[pi] = pj

        for a in A:
            if factors[a]:
                p0 = factors[a][0]
                for p in factors[a][1:]:                # link two primes if they are factors of 'a'
                    union(p2i[p0], p2i[p])

        count = collections.Counter(find(p2i[factors[a][0]]) for a in A if factors[a])      # each 'a' corresponds to a prime index
        return max(count.values())

