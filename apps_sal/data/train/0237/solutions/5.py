class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def atMostK(A, S):
            if S < 0:
                return 0
            i = res = 0

            for j in range(len(A)):
                S -= A[j]
                while S < 0:
                    S += A[i]
                    i += 1
                res += j - i + 1  # 所以小于的也是算了的
            return res
        return atMostK(A, S) - atMostK(A, S - 1)


# 由于数组仅包含 0 和 1， 那么问题可以转化为给定一个0，1数组，你可以选择S个1和任意个0，你可以有多少选择？

# 而上述问题可以转化为给定一个0，1数组，你可以选择最多S个1和任意个0，你的选择数减去 给定一个0，1数组，你可以选择最多S - 1个1和任意个0，你的选择数。

# 最多xxxx 这种可以使用可变滑动窗口模板解决。

# 这道题和前缀和之间的关系是什么呢？


#  At most (s) is the count of subarrays whose sum <= s, at most (s-1) is the count of subarrays whose sum <= s-1, if you subtract them, all you get is subarrays whose sum exactly == s.（前缀和）
