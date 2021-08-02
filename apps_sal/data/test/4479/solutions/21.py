class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        a1 = A
        sum1 = 0
        while K > 0:
            mina = min(a1)
            a1.remove(mina)
            a1.append(mina * (-1))
            K -= 1

        return sum(a1)
