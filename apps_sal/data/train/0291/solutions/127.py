MOD = 10**9 + 7


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_cum_sums = 0
        even_cum_sums = 0

        total_odd_sums = 0
        # Get cumulative sum
        for i in range(len(arr) - 1):
            arr[i + 1] += arr[i]

        for sum_ in arr:
            # Even cumulative sum
            if sum_ % 2 == 0:
                total_odd_sums += odd_cum_sums
                even_cum_sums += 1
            # Odd cumulative sum
            else:
                total_odd_sums += 1 + even_cum_sums
                odd_cum_sums += 1

        return total_odd_sums % MOD

