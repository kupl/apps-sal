class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = 0

        number_odd = 0
        number_even = 0

        total = 0

        for i in arr:
            prefix_sum += i

            if prefix_sum % 2 == 1:
                number_odd += 1
                total += 1
                total += number_even
            else:
                total += number_odd
                number_even += 1

        return int(total % (1e9 + 7))
