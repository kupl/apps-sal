class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:

        def mutated_sum(value):
            cur_sum = 0
            for num in arr:
                if num > value:
                    cur_sum += value
                else:
                    cur_sum += num
            return cur_sum
        left = 1
        right = max(arr)
        while left < right:
            value = left + (right - left) // 2
            cur_sum = mutated_sum(value)
            if cur_sum < target:
                left = value + 1
            else:
                right = value
        s1 = abs(mutated_sum(left - 1) - target)
        print(s1)
        s2 = abs(mutated_sum(left) - target)
        print(s2)
        if s1 <= s2:
            return left - 1
        return left
