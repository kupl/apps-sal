class Solution:

    def numSplits(self, ss: str) -> int:
        a = set()
        k = {}
        p = {}
        n = len(ss)

        def myfunc(s, aa):
            for i in range(n - 1):
                if s[i] not in a:
                    a.add(s[i])
                    aa[i] = 1
                else:
                    aa[i] = 0
                if i != 0:
                    aa[i] += aa[i - 1]
        myfunc(ss, k)
        a.clear()
        myfunc(ss[::-1], p)
        ans = 0
        for j in range(n - 1):
            if k[j] == p[n - 1 - (j + 1)]:
                ans += 1
        return ans
