class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        r = 0
        e = 0
        o = 0
        for i in arr:
            if(i % 2 == 1):
                r += (e + 1)
                o, e = e + 1, o
            else:
                r += o
                o, e = o, e + 1
        a = (10**9) + 7
        return r % a
