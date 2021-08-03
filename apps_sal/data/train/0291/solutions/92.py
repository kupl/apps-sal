class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_sums = 0
        even_sums = 0
        ret = 0
        sum_ = 0

        for num in arr:
            sum_ += num

            if (sum_ & 1):
                ret += even_sums + 1
                odd_sums += 1
            else:
                ret += odd_sums
                even_sums += 1

        return ret % (10 ** 9 + 7)
