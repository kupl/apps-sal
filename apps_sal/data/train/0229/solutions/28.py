from collections import Counter


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        counts = [0] * (10**5 + 1)
        for a in A:
            if a >= 0:
                counts[a] += 1
        for i in range(10**5 + 1):
            while counts[i] != 0:
                counts[i] -= 1
                if counts[i] < 0:
                    return False
                counts[2 * i] -= 1
                if counts[2 * i] < 0:
                    return False
        if not all(n == 0 for n in counts):
            return False

        for a in A:
            if a < 0:
                counts[-a] += 1
        for i in range(10**5 + 1):
            while counts[i] != 0:
                counts[i] -= 1
                if counts[i] < 0:
                    return False
                counts[2 * i] -= 1
                if counts[2 * i] < 0:
                    return False
        if not all(n == 0 for n in counts):
            return False
        return True
