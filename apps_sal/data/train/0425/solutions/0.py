class Solution:
    def get_half(self, dividend, divisor):
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        num = divisor
        num_temp = 0
        result = 1
        result_temp = 0
        while (num <= dividend):
            num_temp = num
            num += num
            result_temp = result
            result += result
        return num_temp, result_temp

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        if divisor == 0:
            return MAX_INT
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        if abs_dividend < abs_divisor:
            return 0
        minus_flag = (dividend is abs_dividend) is (divisor is abs_divisor)
        final_result = 0
        while(abs_dividend >= abs_divisor):
            num, result = self.get_half(abs_dividend, abs_divisor)
            abs_dividend -= num
            final_result += result

        if minus_flag == 1:
            if final_result > MAX_INT:
                return MAX_INT
            return final_result
        else:
            if 0 - final_result < 0 - MAX_INT - 1:
                return 0 - MAX_INT
            return 0 - final_result
