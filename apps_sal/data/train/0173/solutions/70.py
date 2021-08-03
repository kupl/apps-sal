from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = Counter()

        f = 0
        for e in arr:
            ex = (k - (e % k)) % k
            if c[ex] > 0:
                c[ex] -= 1
                f += 1
            else:
                c[e % k] += 1

        return f == len(arr) // 2
