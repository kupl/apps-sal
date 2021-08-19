import numpy as np


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        parents = np.arange(len(A))
        counts = np.ones_like(parents)

        def find(i):
            if parents[i] == i:
                return i
            else:
                return find(parents[i])

        def combine(i, j):
            pi = find(i)
            pj = find(j)
            if pi != pj:
                if counts[pi] > counts[pj]:
                    parents[pj] = pi
                    counts[pi] += counts[pj]
                else:
                    parents[pi] = pj
                    counts[pj] += counts[pi]
        max_prime = int(np.floor(np.sqrt(max(A)))) + 1
        sieve = [True] * (max_prime + 1)
        for prime in range(2, max_prime + 1):
            if sieve[prime]:
                match = -1
                for i in range(len(A)):
                    if A[i] % prime == 0:
                        while A[i] % prime == 0:
                            A[i] = A[i] // prime
                        if match != -1:
                            combine(match, i)
                        else:
                            match = i
                for k in range(prime, max_prime + 1, prime):
                    sieve[k] = False
        inds = np.argsort(A)
        for i in range(1, len(A)):
            if A[inds[i]] != 1 and A[inds[i - 1]] == A[inds[i]]:
                combine(inds[i - 1], inds[i])
        return np.max(counts)
