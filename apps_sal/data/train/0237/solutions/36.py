class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        d = {0: 1}
        ss = 0
        for i in A:
            ss += i
            d[ss] = d.get(ss, 0) + 1
        res = 0
        print(d)
        if S > 0:
            for i in range(ss - S + 1):
                res += d[i] * d[i + S]
        if S == 0:
            for i in range(ss + 1):
                res += d[i] * (d[i] - 1) // 2
        return res
