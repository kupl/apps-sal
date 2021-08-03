class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        freq = dict()
        for i in A:
            freq[i] = freq.get(i, 0) + 1
        for i in A:
            if freq.get(i, 0) == 0:
                continue

            if i < 0:
                if i % 2 != 0:
                    return False
                elif not freq.get(i // 2, 0) > 0:
                    return False
            elif i > 0 and not freq.get(i * 2, 0) > 0:
                return False

            if i < 0:
                freq[i // 2] -= 1
            else:
                freq[i * 2] -= 1
            freq[i] -= 1

        return True
