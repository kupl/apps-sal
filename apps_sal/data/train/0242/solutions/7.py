from collections import Counter, defaultdict


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counter = Counter(nums)
        d = defaultdict(set)
        for x in counter:
            d[counter[x]].add(x)
        i = len(nums)
        while d:
            if len(d) == 1:
                k = list(d.keys())[0]
                if k == 1 or len(d[k]) == 1:
                    return i
            if len(d) == 2:
                y, z = sorted(d.keys())
                if (y == 1 and len(d[y]) == 1) or (y + 1 == z and len(d[z]) == 1):
                    return i
            i -= 1
            x = nums[i]
            d[counter[x]].remove(x)
            if not d[counter[x]]:
                d.pop(counter[x])
            counter[x] -= 1
            if counter[x] > 0:
                d[counter[x]].add(x)
        return 0
