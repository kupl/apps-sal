class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = collections.Counter(A)
        for a in sorted(count, key = lambda x: abs(x)):
            if count[a] > count[2 * a]:
                return False
            count[2 * a] -= count[a]
        return True
