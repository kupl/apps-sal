from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        num_count = Counter(arr)

        sort_nums = list(num_count.most_common())

        while sort_nums and sort_nums[-1][1] <= k:
            k -= sort_nums[-1][1]
            sort_nums.pop()

        return len(sort_nums)
