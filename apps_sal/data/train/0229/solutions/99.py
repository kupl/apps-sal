from collections import Counter


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count_a = Counter(A)
        A.sort(key=lambda x: abs(x))
        for elem in A:
            if count_a[elem] == 0:
                continue
            if count_a[elem * 2] == 0:
                return False
            count_a[elem] -= 1
            count_a[elem * 2] -= 1
        return True
