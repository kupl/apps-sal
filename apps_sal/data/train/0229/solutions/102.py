class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        seen = dict()
        for x in A:
            if x not in seen:
                seen[x] = 0
            seen[x] += 1
        for x in sorted(seen, key=lambda x: x ** 2):
            if seen[x] == 0:
                continue
            if 2 * x not in seen or seen[x] > seen[2 * x]:
                return False
            else:
                seen[2 * x] -= seen[x]
        return True
