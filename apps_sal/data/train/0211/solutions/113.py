class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        ans = 1
        for i in range(2 ** (n - 1)):
            b = '1' + bin(i)[2:].zfill(n - 1) + '1'
            pr = 0
            w = set()
            flag = True
            for k in range(1, n + 1):
                if k == n or b[k] == '1':
                    chrs = s[pr: k]
                    if chrs in w:
                        flag = False
                        break
                    w.add(chrs)
                    pr = k
            if flag:
                ans = max(ans, len(w))
        return ans
