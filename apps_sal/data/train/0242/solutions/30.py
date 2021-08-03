class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        d = Counter(nums)
        # print(d)

        for i in reversed(range(len(nums))):
            vlist = list(d.values())
            # print(vlist)
            s = list(set(vlist))

            if len(s) == 1:
                if s[0] == 1:
                    return i + 1
                if len(vlist) == 1:
                    return i + 1

            if len(s) == 2:
                if 1 in s:
                    if vlist.count(1) == 1:
                        return i + 1

                maxint = max(s[0], s[1])
                if vlist.count(maxint) == 1 and abs(s[1] - s[0]) == 1:
                    return i + 1

            if d[nums[i]] == 1:
                d.pop(nums[i])
            else:
                d[nums[i]] -= 1

        return 1
