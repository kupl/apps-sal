class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            parent[px] = py
        div_bucket = collections.defaultdict(list)

        def findDivisor(num):
            if num < 2:
                return set()
            for div in range(2, int(math.sqrt(num)) + 2):
                if num % div == 0:
                    return findDivisor(num // div) | {div}
            return {num}
        for i in range(n):
            div_set = set()
            div_set = findDivisor(A[i])
            for div in div_set:
                div_bucket[div].append(i)
        for (_, nums) in list(div_bucket.items()):
            for j in range(len(nums) - 1):
                union(nums[j], nums[j + 1])
        return max(collections.Counter([find(x) for x in range(n)]).values())
