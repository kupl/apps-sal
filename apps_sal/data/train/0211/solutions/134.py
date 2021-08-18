class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        to_ret = 0
        for bin_i in range(2**(len(s) - 1)):
            to_deal = []
            last = s[0]
            for i in range(len(s) - 1):
                cn = s[i + 1]
                if (bin_i & (1 << i)) > 0:
                    to_deal.append(last)
                    last = cn
                else:
                    last += cn
            if not last == '':
                to_deal.append(last)
            if len(to_deal) == len(set(to_deal)):
                to_ret = max(to_ret, len(to_deal))
        return to_ret
