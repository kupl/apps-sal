class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        from collections import defaultdict
        modulo = defaultdict(int)
        large_factor = 100000000.0
        for (i, v) in enumerate(arr):
            modulo[(v + large_factor * k) % k] += 1
        for (mod, cnt) in list(modulo.items()):
            if mod == 0 and cnt % 2 != 0:
                return False
            if modulo[(k - mod % k) % k] != cnt:
                return False
        return True
