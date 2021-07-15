class Solution:
    def numWays(self, s: str) -> int:
        total, res, n = 0, 0, len(s)
        for ch in s:
            if ch == '1':
                total += 1
        if total % 3 != 0: return res
        if total == 0: return (math.factorial(n - 1) // math.factorial(n - 3) // 2) % (10**9 + 7)
        l, r, cnt = 0, 0, 0
        for i,ch in enumerate(s):
            if ch == '1': 
                cnt += 1
                if cnt == (total // 3): 
                    l = i
            if cnt == (total // 3) + 1:
                r = i
                break
        res = (r - l) % (10**9 + 7)
        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == '1': 
                cnt += 1
                if cnt == (total // 3): 
                    r = i
            if cnt == (total // 3) + 1:
                l = i
                break
        res *= (r - l)
        return res % (10**9 + 7)
