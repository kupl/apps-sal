class Solution:
    #     def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
    #         neighcount = [0,0,0,0,0]
    #         minhorses = 0
    #         nstarted = 0
    #         nended = 0

    #         for s in croakOfFrogs:
    #             if s == 'c':
    #                 neighcount[0] += 1
    #                 nstarted += 1
    #             elif s == 'r':
    #                 neighcount[1] += 1
    #                 neighcount[0] -= 1
    #                 if neighcount[0] < 0:
    #                     return -1
    #             elif s == 'o':
    #                 neighcount[2] += 1
    #                 neighcount[1] -= 1
    #                 if neighcount[1] < 0:
    #                     return -1
    #             elif s == 'a':
    #                 neighcount[3] += 1
    #                 neighcount[2] -= 1
    #                 if neighcount[2] < 0:
    #                     return -1
    #             elif s == 'k':
    #                 neighcount[4] += 1
    #                 neighcount[3] -= 1
    #                 nstarted -= 1
    #                 if neighcount[3] < 0:
    #                     return -1
    #             else:
    #                 return -1
    #             if nstarted > minhorses:
    #                 minhorses = nstarted
    #         neighcount[4] = 0
    #         if max(neighcount) == 0:
    #             return minhorses
    #         else:
    #             return -1
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        if len(croakOfFrogs) % 5 != 0 or croakOfFrogs[0] != 'c' or croakOfFrogs[-1] != 'k':
            return -1

        max_frog_croak = 0
        present_frog_croak = 0

        d = {}
        d['c'] = 0
        d['r'] = 0
        d['o'] = 0
        d['a'] = 0
        d['k'] = 0

        for ch in croakOfFrogs:
            d[ch] += 1
            if ch == 'c':
                present_frog_croak += 1
            if ch == 'k':
                present_frog_croak -= 1

            max_frog_croak = max(max_frog_croak, present_frog_croak)

        if d['c'] != d['r'] or d['r'] != d['o'] or d['o'] != d['a'] or d['a'] != d['k']:
            return -1

        return max_frog_croak
