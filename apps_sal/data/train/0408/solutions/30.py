class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        # sum_of_mutate(arr, sorted_arr[i]) will be like
        # L L L L M M
        # where L = sum_of_mutate[i] less than or equal target, M = more
        # we want to find last L
        # then answer can be last L or next M whatever make mutate sum smaller

        l = 0
        r = max(arr)

        while l < r:
            mid = ((l + r) // 2) + 1

            if sum(min(e, mid) for e in arr) > target:
                r = mid - 1
            else:
                l = mid

        # then answer can be last L or next M whatever make mutate sum smaller
        # use less or equal because if it ties, we will choose smaller
        if abs(sum(min(e, l) for e in arr) - target) <= abs(sum(min(e, l + 1) for e in arr) - target):
            return l
        else:
            return l + 1
