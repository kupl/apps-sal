class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        (o, e) = (0, 0)
        res = 0
        for n in arr:
            if n % 2 == 0:
                e += 1
            else:
                (o, e) = (e, o)
                o += 1
            res += o
            res = res % (10 ** 9 + 7)
        return res
