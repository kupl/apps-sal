class Solution:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        total = sum(A)
        sets = [{0}] + [set() for _ in A]
        for num in A:
            for j in reversed(list(range(len(A) - 1))):
                for k in sets[j]:
                    s = k + num
                    if total * (j + 1) == s * len(A):
                        return True
                    sets[j + 1].add(k + num)
        return False
