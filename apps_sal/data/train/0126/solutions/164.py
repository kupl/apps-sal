import operator


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        lp = 0
        rp = lp + minSize
        perm_dict = {}
        for i in range(len(s) - minSize + 1):
            temp = s[lp:rp]
            if len(set(temp)) <= maxLetters:
                if temp not in list(perm_dict.keys()):
                    perm_dict[temp] = 1
                else:
                    perm_dict[temp] += 1
            i += 1
            lp += 1
            rp += 1
        print(perm_dict)
        perm_dict = dict(sorted(list(perm_dict.items()), key=operator.itemgetter(1), reverse=True))
        if len(list(perm_dict.keys())) > 0:
            return perm_dict[list(perm_dict.keys())[0]]
        return 0
