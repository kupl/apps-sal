class Solution:

    def minKBitFlips(self, a: List[int], k: int) -> int:
        n = len(a)
        toggles = [0] * (n + 1)  # toggles[i] is 1 if we should toggle our view
        min_flips = 0
        view = 0  # 0 means normal, 1 means inverted

        for i, b in enumerate(a):
            # If we're ending an interval where we've previously flipped, toggle
            # our view
            view ^= toggles[i]
            if b ^ view == 0:  # This value is 0, we've gotta flip it
                if i + k > n:  # No way to flip to fix this (can't be done)
                    return -1
                min_flips += 1
                view ^= 1  # toggle our view (view things from now on as flipped)
                toggles[i + k] ^= 1  # toggle our view back once we get to i + k
        return min_flips
