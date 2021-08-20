class Solution:

    def numWays(self, s: str) -> int:
        count1s = len([x for x in s if x == '1'])
        if count1s % 3:
            return 0
        if not count1s:
            return (len(s) - 1) * (len(s) - 2) // 2 % 1000000007
        idx1 = -1
        idx2 = -1
        idx3 = -1
        idx4 = -1
        ct = 0
        for (i, c) in enumerate(s):
            if c == '1':
                ct += 1
            if ct == count1s // 3 and idx1 == -1:
                idx1 = i
            if ct == count1s // 3 + 1 and idx2 == -1:
                idx2 = i
            if ct == 2 * (count1s // 3) and idx3 == -1:
                idx3 = i
            if ct == 2 * (count1s // 3) + 1 and idx4 == -1:
                idx4 = i
        return (idx2 - idx1) * (idx4 - idx3) % 1000000007
