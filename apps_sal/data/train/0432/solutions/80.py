from collections import OrderedDict, Counter


class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        elems = sorted(list(set(nums)))
        count = OrderedDict()
        for elem in elems:
            count[elem] = 0
        for num in nums:
            count[num] += 1
        while len(count) > 0:
            x = list(count.keys())[0]
            for i in range(x, x + k):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    del count[i]
        return True
