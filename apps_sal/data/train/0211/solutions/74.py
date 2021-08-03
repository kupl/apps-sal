class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def divide(s):
            for i in range(1, len(s)):
                low = s[0: i]
                high = s[i:]
                yield (low, high)
                for div in divide(high):
                    ret = [low]
                    ret.extend(div)
                    yield ret

        combinations = list(divide(s))
        combinations.append(s)
        # print(combinations)
        ret = 1
        for comb in combinations:
            if len(comb) == len(set(comb)):
                # print(comb, set(comb))
                ret = max(ret, len(comb))
        return ret
