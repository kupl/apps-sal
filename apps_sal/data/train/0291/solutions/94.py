class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        even_sums = []
        odd_sums = []
        current_sum = 0
        for i in range(len(arr)):
            current_sum += arr[i]
            if current_sum % 2 == 0:
                # is even
                # if odd_sums[-1]
                # if len(odd_sums) > 0:
                #     ans += i - odd_sums[-1]
                ans += len(odd_sums)

                even_sums.append(i)
            else:
                # is odd
                # ans += 1
                ans += 1 + len(even_sums)
                # j = 1
                # while j <= len(even_sums) and even_sums[-j] == i-1
                #     if
                #     j += 1
                # if len(even_sums) > 0 and even_sums[-1] == i-1:
                #     ans += 1
                # if len(odd_sums) > 0:
                #     ans += i - odd_sums[-1] + 1
                # else:
                #     ans += i
                # ans += len([])
                # last odd
                # odd_sums[-1]
                odd_sums.append(i)
        return ans % (10**9 + 7)


if True:
    print((Solution().numOfSubarrays([1, 2, 3, 4, 5, 6, 7])))  # 16
    print((Solution().numOfSubarrays([100, 100, 99, 99])))  # 4
    print((Solution().numOfSubarrays([7])))  # 1
    print((Solution().numOfSubarrays([2, 4, 6])))  # 0


# [1,2,3,4,5,6,7]
# [1]
# [1,2]
# [1]

# [1,3,5]
# 1, 1,

# [2,4,6]
# 0

# set(100), set(99), 200
# [100,100,99,99]
# 1 + 1 + 1

# [1,2,3,4,5,6,7]
# 1 + 1 + 1 + 1 set(1,3) set(2)
