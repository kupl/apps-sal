from collections import Counter


class Solution:

    def numSplits(self, s: str) -> int:
        l_dict = Counter()
        r_dict = Counter(s)
        counter = 0
        print(r_dict)
        for i in s:
            r_dict[i] -= 1
            l_dict[i] = l_dict.get(i, 0) + 1
            if r_dict[i] == 0:
                del r_dict[i]
            if len(l_dict) == len(r_dict):
                counter += 1
        return counter
