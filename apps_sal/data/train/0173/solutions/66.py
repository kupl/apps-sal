from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        matches = Counter()

        c = 0
        for e in arr:
            me = -e % k
            if matches[me] > 0:
                matches[me] -= 1
                c += 1
            else:
                matches[e % k] += 1

        return c == len(arr) // 2
