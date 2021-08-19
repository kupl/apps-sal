class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        mp = {}
        sum_list = 0
        mp[0] = -1
        for i, val in enumerate(arr):
            sum_list += val
            mp[sum_list] = i

        res = float('inf')
        lvalue = float('inf')
        sum_list = 0
        # print(mp)

        for i, val in enumerate(arr):
            sum_list += val
            if sum_list - target in mp:
                lvalue = min(lvalue, i - mp[sum_list - target])

            if sum_list + target in mp and lvalue != float('inf'):
                res = min(res, lvalue + mp[sum_list + target] - i)

        return -1 if res == float('inf') else res
