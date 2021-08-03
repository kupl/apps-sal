class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        for is_pos, group in itertools.groupby(nums, key=bool):
            if is_pos:
                subgroup = list(group)
                num_negs = 0
                # if the num negs is odd, the answer is either
                # the length without the first negative
                # or the length without the last negative
                first = last = None
                for i, n in enumerate(subgroup):
                    if n < 0:
                        num_negs += 1
                        if first is None:
                            first = i
                        last = i
                if num_negs % 2 == 0:
                    res = max(res, len(subgroup))
                else:
                    res = max(res, first, len(subgroup) - 1 - first)
                    res = max(res, last, len(subgroup) - 1 - last)
        return res
