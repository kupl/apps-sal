class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        counter = collections.Counter(A)
        for x in sorted(counter, key=abs):
            if counter[x] > counter[2 * x]:
                return False
            counter[2 * x] -= counter[x]
        return True
