class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        arr_of_powers = {}

        def get_int_power(num):

            pwr = 0
            temp = num
            while temp != 1:
                pwr += 1
                if temp % 2 == 0:
                    temp /= 2
                elif temp % 2 == 1:
                    temp = 3 * temp + 1
            return pwr

        for num in range(lo, hi + 1):
            arr_of_powers[num] = get_int_power(num)

        interval = sorted(arr_of_powers.items(), key=lambda x: x[1])

        return interval[k - 1][0]
