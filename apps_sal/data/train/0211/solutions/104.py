class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        to_ret = 0
        for bin_i in range(2 ** (len(s) - 1)):
            to_deal = set()
            mark = True
            last = s[0]
            for i in range(len(s) - 1):
                cn = s[i + 1]
                if bin_i & 1 << i > 0:
                    if last in to_deal:
                        mark = False
                        break
                    to_deal.add(last)
                    last = cn
                else:
                    last += cn
            if last in to_deal:
                mark = False
            else:
                to_deal.add(last)
            if mark:
                to_ret = max(to_ret, len(to_deal))
        return to_ret
