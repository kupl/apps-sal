from sortedcontainers import SortedList


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        B = [nums[i] for i in range(len(nums))]
        store = SortedList()

        for i in range(len(nums) - 1, -1, -1):
            if len(store) > 0:
                if store[-1] > 0:
                    B[i] += store[-1]

            store.add(B[i])
            if len(store) > k:
                store.remove(B[i + k])

        return max(B)
