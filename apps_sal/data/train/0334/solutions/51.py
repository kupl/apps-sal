class Solution:
    from collections import defaultdict

    def minCost(self, s: str, cost: List[int]) -> int:
        _dic = defaultdict(list)
        start, end = 0, 0
        s = s + '$'

        for ind in range(0, len(s) - 1):
            if s[ind] == s[ind + 1]:
                end += 1
            else:
                if start != end:
                    _dic[s[ind]].append((start, end))
                start = end + 1
                end += 1

        res = 0

        for key in _dic:
            for tup in _dic[key]:
                res += sum(sorted(cost[tup[0]:tup[1] + 1])[:(tup[1] - tup[0])])

        return res
