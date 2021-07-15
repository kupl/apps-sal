import collections as clc


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 == 1:
            return False
        counts = clc.Counter([v % k for v in arr])
        if k % 2 == 0:
            if counts[k // 2] % 2 != 0:
                return False
        return all(counts[i] == counts[k - i] for i in range(1, k // 2 + 1))
