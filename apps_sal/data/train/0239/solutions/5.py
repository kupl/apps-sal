class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        label2values = defaultdict(list)
        for (value, label) in zip(values, labels):
            label2values[label].append(value)
        all_top_nums = []
        for values in list(label2values.values()):
            if use_limit >= len(values):
                top_nums = values
            else:
                top_nums = self.quick_select(use_limit, values)
            all_top_nums.extend(top_nums)
        if num_wanted >= len(all_top_nums):
            return sum(all_top_nums)
        return sum(self.quick_select(num_wanted, all_top_nums))

    def quick_select(self, use_limit, nums):
        low = 0
        high = len(nums) - 1
        use_limit -= 1
        while low <= high:
            pivot = self.partition(nums, low, high)
            if pivot == use_limit:
                return nums[:pivot + 1]
            elif pivot < use_limit:
                low = pivot + 1
            else:
                high = pivot - 1
        return nums

    def partition(self, nums, low, high):
        pivot = random.randint(low, high)
        self._swap(nums, pivot, high)
        pivot = low
        for i in range(low, high):
            if nums[i] > nums[high]:
                self._swap(nums, pivot, i)
                pivot += 1
        self._swap(nums, pivot, high)
        return pivot

    def _swap(self, nums, i, j):
        (nums[i], nums[j]) = (nums[j], nums[i])
