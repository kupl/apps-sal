class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        for i in nums:
            for ind, j in enumerate(bin(i)[2:][::-1]):
                if j == '1':
                    cache[ind] += 1
        return sum(cache.values()) + max(cache.keys())
