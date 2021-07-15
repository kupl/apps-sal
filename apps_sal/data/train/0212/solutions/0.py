class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        
        mod = 10**9 + 7

        nums_set = set(A)
        nums = A.copy()
        nums.sort()
        counts = {}
        total = 0

        for n in nums:
            n_count = 1
            for d in nums:
                if d * d > n:
                    break
                if n % d != 0:
                    continue
                e = n // d
                if e not in nums_set:
                    continue

                subtrees = (counts[d] * counts[e]) % mod
                if d != e:
                    subtrees = (subtrees * 2) % mod
                n_count = (n_count + subtrees) % mod
            counts[n] = n_count % mod
            total = (total + n_count) % mod

        return total

