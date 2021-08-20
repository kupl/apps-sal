class Solution:

    def minOperations(self, nums: List[int]) -> int:
        even_num = []
        odd_num = []
        zero_num = []

        def category(n, zero_num, even_num, odd_num):
            if n == 0:
                zero_num.append(n)
            elif n % 2 == 0:
                even_num.append(n)
            else:
                odd_num.append(n)
        for n in nums:
            category(n, zero_num, even_num, odd_num)
        ans = 0
        while len(even_num) or len(odd_num):
            new_odd_num = []
            if len(odd_num):
                ans += len(odd_num)
            for n in odd_num:
                n = n - 1
                category(n, zero_num, even_num, new_odd_num)
            odd_num = new_odd_num
            new_even_num = []
            if len(even_num):
                ans += 1
            for n in even_num:
                n = n // 2
                category(n, zero_num, new_even_num, odd_num)
            even_num = new_even_num
        return ans
