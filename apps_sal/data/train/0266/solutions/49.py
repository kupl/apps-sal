class Solution:
    def numSplits(self, ss: str) -> int:
        a = set()
        k = {}
        p = {}
        n = len(ss)

        def myfunc(s, aa):
            for i in range(n - 1):
                if(s[i] not in a):
                    a.add(s[i])
                    aa[i] = 1
                else:
                    aa[i] = 0
                if(i != 0):
                    aa[i] += aa[i - 1]
        myfunc(ss, k)  # k[i] gives,no of distinct letters,to left of left of index i+1 in ss
        a.clear()
        myfunc(ss[::-1], p)  # p[i] gives,no of distinct letters,to left of left of index i+1...in ss_reverse
        ans = 0
        # print(k)
        # print(p)
        for j in range(n - 1):
            if(k[j] == p[n - 1 - (j + 1)]):
                ans += 1

        return ans
