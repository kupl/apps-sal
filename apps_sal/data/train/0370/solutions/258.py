class Solution:

    def largestComponentSize(self, nums: List[int]) -> int:
        uf = {}

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf.setdefault(x, x)
            uf.setdefault(y, y)
            uf[find(x)] = uf[find(y)]
        for num in nums:
            union(num, num)
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    union(num, i)
                    union(num // i, i)
        group_counter = collections.Counter()
        for num in nums:
            group_counter[find(num)] += 1
        return max(group_counter.values())
