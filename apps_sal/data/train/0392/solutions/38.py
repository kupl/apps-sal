class Solution:

    def numWays(self, s: str) -> int:
        one_cnt = 0

        def dfs(s, num, start, left):
            ans = 0
            for i in range(start, len(s)):
                if s[i] == '1':
                    one_cnt += 1
                if one_cnt == num:
                    ans += dfs(s, num, i + 1, left - 1)
                    ans = ans % (10 ** 9 + 7)
            return ans
        one_cnt = Counter(s)['1']
        if one_cnt % 3 != 0:
            return 0
        if one_cnt == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % (10 ** 9 + 7)
        num = one_cnt / 3
        i = 0
        cnt = 0
        while cnt < num:
            if s[i] == '1':
                cnt += 1
            i += 1
        start = i
        while i < len(s) and s[i] == '0':
            i += 1
        first = i - start + 1
        cnt2 = 0
        while cnt2 < num:
            if s[i] == '1':
                cnt2 += 1
            i += 1
        start2 = i
        while i < len(s) and s[i] == '0':
            i += 1
        second = i - start2 + 1
        ans = first * second % (10 ** 9 + 7)
        return ans
