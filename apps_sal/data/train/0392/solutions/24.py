class Solution:
    def numWays(self, s: str) -> int:
        nums = [0] * len(s)
        cum = 0
        hh = Counter()
        for i in range(len(s)):
            if s[i] == '1':
                cum += 1
            nums[i] = cum
            hh[cum] += 1
        if cum % 3 != 0:
            return 0
        if cum == 0:
            return int(math.comb(hh[0] - 1, 2)) % (1000000007)
        each = cum // 3
        print((hh, each))
        return int(hh[each] * hh[2 * each] % (1000000007))
