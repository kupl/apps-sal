class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        even_sums = []
        odd_sums = []
        current_sum = 0
        for i in range(len(arr)):
            current_sum += arr[i]
            if current_sum % 2 == 0:
                ans += len(odd_sums)
                even_sums.append(i)
            else:
                ans += 1 + len(even_sums)
                odd_sums.append(i)
        return ans % (10 ** 9 + 7)


if True:
    print(Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))
    print(Solution().numOfSubarrays([100, 100, 99, 99]))
    print(Solution().numOfSubarrays([7]))
    print(Solution().numOfSubarrays([2, 4, 6]))
