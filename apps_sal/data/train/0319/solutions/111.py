class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        ts = sum(stoneValue)
        n = len(stoneValue)

        a = [0 for i in range(n)]
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                a[i] = stoneValue[i]
            else:
                a[i] = a[i + 1] + stoneValue[i]

        cache = {}

        def process(i):
            if i == n:
                return 0
            else:
                if not i in cache:
                    ans = -float('inf')
                    if i < n:
                        ans = max(ans, stoneValue[i] + (a[i + 1] - process(i + 1) if i + 1 < n else 0))
                    if i + 1 < n:
                        ans = max(ans, stoneValue[i] + stoneValue[i + 1] + (a[i + 2] - process(i + 2) if i + 2 < n else 0))
                    if i + 2 < n:
                        ans = max(ans, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + (a[i + 3] - process(i + 3) if i + 3 < n else 0))
                    cache[i] = ans
                return cache[i]

        Alice = process(i)
        Bob = ts - Alice
        if Alice > Bob:
            return 'Alice'
        elif Bob > Alice:
            return 'Bob'
        else:
            return 'Tie'
