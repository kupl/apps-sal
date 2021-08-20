class Solution:

    def longestOnes(self, a: List[int], K: int) -> int:
        i = 0
        j = 0
        ml = 0
        while i < len(a):
            if a[i] == 0:
                K -= 1
            while K < 0:
                if a[j] == 0:
                    K += 1
                j += 1
            ml = max(ml, i - j + 1)
            i += 1
        return ml
