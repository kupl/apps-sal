class Solution:
    def minOperations(self, nums):
        ans = 0
        maxtimes = 0
        for num in nums:
            plus, times = 0, 0
            # print(num)
            while num != 0:
                plus = plus + num % 2
                if num // 2 != 0:
                    times += 1
                num = num // 2

            maxtimes = max(maxtimes, times)
            #print(num, plus, times)
            ans = ans + plus

        ans += maxtimes
        return(ans)


x = Solution()
print(x.minOperations([1, 5]))
