class Solution:

    def minKBitFlips(self, a: List[int], k: int) -> int:
        n = len(a)
        toggles = [0] * (n + 1)
        min_flips = 0
        view = 0

        for i, b in enumerate(a):
            view ^= toggles[i]
            if b ^ view == 0:
                if i + k > n:
                    return -1
                min_flips += 1
                view ^= 1
                toggles[i + k] ^= 1
        return min_flips
