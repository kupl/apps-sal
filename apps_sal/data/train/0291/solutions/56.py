class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        (c, e, o, a) = (0, 1, 0, 0)
        for i in arr:
            c += i
            if c % 2 == 0:
                a += o
                a %= 1000000007
                e += 1
            else:
                a += e
                a %= 1000000007
                o += 1
        return a % 1000000007
