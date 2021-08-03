class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        pow_sigs = set()
        twon = 1
        while twon <= 10**9:
            sig = [0] * 10
            s = str(twon)
            for c in s:
                sig[int(c)] += 1

            pow_sigs.add(tuple(sig))
            twon *= 2

        n_sig = [0] * 10
        s = str(N)
        for c in s:
            n_sig[int(c)] += 1

        if tuple(n_sig) in pow_sigs:
            return True
        else:
            return False
