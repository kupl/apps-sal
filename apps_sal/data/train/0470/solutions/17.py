from collections import Counter


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        mp = Counter(A)
        total = 0
        mpow = 10**9 + 7
        for i in range(101):
            for j in range(i, 101):
                calc = target - (i + j)
                if calc > 100 or calc < 0:
                    continue
                if i == j == calc:
                    x = mp[i]
                    top_row = x * (x - 1) * (x - 2)
                    top_row /= 6
                    total += top_row
                elif i == j != calc:
                    x = mp[i]
                    total += ((x * (x - 1)) / 2) * mp[calc]
                elif i < j < calc:
                    total += mp[i] * mp[j] * mp[calc]
        return int(total % mpow)
