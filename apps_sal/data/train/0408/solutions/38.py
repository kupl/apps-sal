class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0] if arr[0] <= target else target
        value = 1
        sum_up = 0
        index = 0
        last_sum = 0
        arr.sort()
        while value < arr[-1]:

            current_sum = 0
            while value >= arr[index]:
                sum_up += arr[index]
                index += 1
            current_sum = sum_up + ((len(arr) - index) * value)
            if current_sum == target:
                return value
            elif current_sum > target:
                if abs(last_sum - target) <= abs(current_sum - target):
                    return value - 1
                else:
                    return value
            else:
                last_sum = current_sum
            value += 1

        return value
