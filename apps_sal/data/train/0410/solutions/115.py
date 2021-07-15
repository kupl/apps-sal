class Solution:
        def getKth(self, lo: int, hi: int, k: int) -> int:
                def getPower(num: int) -> int:
                        if num == 1: return 0
                        if num % 2 == 0: return 1 + getPower(num // 2)
                        if num % 2 == 1: return 1 + getPower(3 * num + 1)

                powers = []
                for cand in range(lo, hi + 1):
                        powers.append((cand, getPower(cand)))

                powers = sorted(powers, key=lambda x: x[1])
                return powers[k - 1][0]
