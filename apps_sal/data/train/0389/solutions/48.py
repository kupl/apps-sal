class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        ksums = [{0}]
        maxk = len(A) // 2

        n = len(A)
        S = sum(A)
        for a in A:
            nksums = [[0]]
            for k in range(1, min(len(ksums), maxk) + 1):
                row = (ksums[k] if k < len(ksums) else set()) | {a + x for x in ksums[k - 1]}
                if any(x * (n - k) == k * (S - x) for x in row):
                    return True

                nksums.append(row)

            ksums = nksums

        return False
