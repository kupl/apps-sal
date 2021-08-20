class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        count = collections.Counter(A)
        for i in sorted(count, key=abs):
            count[2 * i] -= count[i]
            if count[2 * i] < 0:
                return False
        return True
