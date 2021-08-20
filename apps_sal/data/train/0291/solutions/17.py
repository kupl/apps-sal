class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        sums = [0]
        sum = 0
        for n in arr:
            sum += n
            sums.append(sum)
        odd_sum_count = []
        even_sum_count = []
        odd_sum = 0
        even_sum = 0
        for ss in sums:
            odd_sum += 1 if ss % 2 == 1 else 0
            even_sum += 0 if ss % 2 == 1 else 1
            odd_sum_count.append(odd_sum)
            even_sum_count.append(even_sum)
        ans = 0
        for i in range(len(arr)):
            if sums[i + 1] % 2 == 0:
                ans += odd_sum_count[i]
            else:
                ans += even_sum_count[i]
            ans = ans % (10 ** 9 + 7)
        return ans
