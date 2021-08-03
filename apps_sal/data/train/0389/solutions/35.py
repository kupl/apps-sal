class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        ksums = [{0}]
        maxk = len(A) // 2

        for a in A:
            #print('a', a)
            #print('ksums', ksums)
            ksums = [[0]] + [
                (ksums[k] if k < len(ksums) else set()) |
                {a + x for x in ksums[k - 1]}
                for k in range(1, min(len(ksums), maxk) + 1)
            ]
            #print('ksums*', ksums)

        n = len(A)
        S = sum(A)
        for k in range(1, min(len(ksums), maxk) + 1):
            if any(x * (n - k) == k * (S - x) for x in ksums[k]):
                return True

        return False
