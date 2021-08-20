import collections


class Solution:

    def numWays(self, s):
        count = collections.Counter(s)
        if count['1'] == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % (10 ** 9 + 7)
        if count['1'] < 3 or count['1'] % 3 != 0:
            return 0
        ans = 1
        cur = 0
        expand = 1
        find = count['1'] // 3
        slot = 0
        for ss in s:
            if slot == 2:
                return ans * expand
            if find > cur:
                if ss == '1':
                    cur += 1
            elif ss == '0':
                expand += 1
            else:
                ans *= expand
                expand = 1
                cur = 1
                slot += 1
        ans *= expand
        return ans % (10 ** 9 + 7)
