class DSU:

    def __init__(self, nums):
        self.nums = [i for i in range(len(nums))]
        self.cnt = [1] * len(nums)

    def find(self, idx):
        if self.nums[idx] == idx:
            return idx
        pidx = self.find(self.nums[idx])
        self.nums[idx] = pidx
        return pidx

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px != py:
            self.nums[px] = self.nums[py]
            self.cnt[py] += self.cnt[px]
        return self.cnt[py]


class Solution:

    def primes_set(self, x):
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return self.primes_set(x // i) | set([i])
        return set([x])

    def largestComponentSize(self, A: List[int]) -> int:
        dsu = DSU(A)
        primes = {}
        for (i, x) in enumerate(A):
            for prime in self.primes_set(x):
                if prime not in primes:
                    primes[prime] = []
                primes[prime].append(i)
        ans = 0
        for (_, idxs) in list(primes.items()):
            for i in range(len(idxs) - 1):
                ans = max(ans, dsu.union(idxs[i], idxs[i + 1]))
        return ans
