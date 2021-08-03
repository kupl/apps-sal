class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def check(n):
            i = 1
            cnt = 0
            res = 0
            while i * i < n:
                if n % i == 0:
                    cnt += 2
                    res += i
                    res += n // i
                i += 1
                if cnt > 4:
                    return 0
            if i * i == n:
                cnt += 1
                res += i
            if cnt == 4:
                return res
            else:
                return 0

        # print (check(21))
        # return 1
        res = sum(check(n) for n in nums)
        return res
