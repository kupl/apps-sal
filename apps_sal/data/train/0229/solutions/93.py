from collections import Counter

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        # Greedy
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        count = Counter(A)
        for x in sorted(A, key=abs):
            if count[x] == 0: continue
            if count[2 * x] == 0: return False
            count[x] -= 1
            count[2 * x] -= 1
        return True

