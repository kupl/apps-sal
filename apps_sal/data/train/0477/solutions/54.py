bins = [[0]]
for _ in range(20):
    bins.append(bins[-1] + [1] + [1 - x for x in reversed(bins[-1])])


class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        return str(bins[n - 1][k - 1])
