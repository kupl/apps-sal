class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = collections.Counter(A)
        for x in sorted(A, key=abs):
            if count[x] == 0:
                continue
            if x == 0 and x % 2:
                return False
            if count[x] > count[2 * x]:
                return False
            count[x], count[2 * x] = 0, count[2 * x] - count[x]

        return True
