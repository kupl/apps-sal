class Solution:

    def numSplits(self, s: str) -> int:
        left = sorted([s.find(l) for l in set(s)]) + [len(s)]
        right = sorted([s.rfind(l) for l in set(s)], reverse=True) + [0]
        ind = max((ind for ind in range(len(left)) if left[ind] <= right[ind]))
        return min(right[ind], left[ind + 1]) - max(left[ind], right[ind + 1])


'\n"aacaba"\n"abcd"\n"aaaaa"\n"acbadbaada"\n"a"\n"abc"\n"abcd"\n'
