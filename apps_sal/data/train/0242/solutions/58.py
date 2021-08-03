
class Solution:
    def maxEqualFreq(self, nums) -> int:
        '''

        :param nums: : List[int]
        :return:
        '''

        n = len(nums)
        a = Counter(nums)

        # print(nums)
        for i in range(n - 1, 0, -1):
            if len(a) == 1:
                p = [i for i in list(a.keys())][0]
                return a[p]
            b = Counter(list(a.values()))

            if len(b) > 2:
                a[nums[i]] -= 1
                if not a[nums[i]]:
                    a.pop(nums[i])
                continue
            elif len(b) == 1:
                if 1 in list(a.values()):
                    return i + 1
                return i
            elif len(b) == 2:
                if 1 in list(b.keys()) and b[1] == 1:
                    return i + 1
                if 1 in list(b.values()):
                    mia, aa = [la for la in list(b.keys())]
                    mia, aa = min(mia, aa), max(mia, aa)
                    if b[aa] == 1 and aa - mia == 1:
                        return i + 1
                    a[nums[i]] -= 1
                    if not a[nums[i]]:
                        a.pop(nums[i])
                else:
                    a[nums[i]] -= 1
                    if not a[nums[i]]:
                        a.pop(nums[i])
                    continue
