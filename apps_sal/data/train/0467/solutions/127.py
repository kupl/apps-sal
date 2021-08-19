class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        range_6 = list(range(6))
        result = 0
        for num in nums:
            if num in range_6:
                pass
            else:
                pivot = int(num ** 0.5)
                temp = 1 + num
                len_t = 2
                for i in range(2, pivot + 1):
                    (divisor, rem) = divmod(num, i)
                    if not rem:
                        if i == divisor:
                            len_t = 0
                            break
                        temp += i + divisor
                        len_t += 2
                        if len_t > 4:
                            break
                if len_t == 4:
                    result += temp
        return result
