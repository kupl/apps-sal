class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        counter = Counter(A)
        for a in sorted(A, key=abs):
            if counter[a] == 0:
                continue
            if counter[2 * a] == 0:
                return False
            counter[a] -= 1
            counter[2 * a] -= 1
        return True
