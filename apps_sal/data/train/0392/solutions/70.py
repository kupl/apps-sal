class Solution:

    def numWays(self, s: str) -> int:
        cnt = 0
        ans = 0
        n = len(s)
        m = 1000000007
        for i in range(len(s)):
            if s[i] == '1':
                cnt += 1
        if cnt == 0:
            ans = (n - 1) * (n - 2) / 2
            ans = ans % m
            return int(ans)
        else:
            hm = dict()
            cnt = 0
            ans = 0
            for i in range(len(s)):
                if s[i] == '1':
                    cnt += 1
                if cnt not in hm.keys():
                    hm[cnt] = 1
                else:
                    hm[cnt] = hm[cnt] + 1
            if cnt % 3 != 0:
                return 0
            else:
                first = hm[cnt / 3]
                tthird = cnt / 3 * 2
                second = hm[tthird]
                ans = first % m * (second % m) % m
            return int(ans)
