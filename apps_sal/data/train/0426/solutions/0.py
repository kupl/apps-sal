class Solution:

    def reorderedPowerOf2(self, n: int) -> bool:
        n_len = len(str(n))
        n = Counter(str(n))
        p = 1
        while len(str(p)) <= n_len:
            if len(str(p)) == n_len and Counter(str(p)) == n:
                return True
            p *= 2
        return False
