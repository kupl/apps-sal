class Solution:

    def numWays(self, s: str) -> int:
        M = 10 ** 9 + 7
        count = collections.Counter(s)
        print(count)
        cnt = count['1']
        if cnt % 3 != 0:
            return 0
        if cnt == 0:
            return comb(len(s) - 1, 2) % M
        target = cnt // 3
        (left, mid, right) = (0, 0, 0)
        cur = 0
        for i in range(len(s)):
            if s[i] == '1':
                cur += 1
            if cur == target:
                left += 1
            elif cur == target * 2:
                mid += 1
        print((left, mid, right))
        return left * mid % M
