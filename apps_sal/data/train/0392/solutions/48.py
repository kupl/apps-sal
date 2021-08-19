class Solution:

    def numWays(self, s: str) -> int:

        def nice_multiply(a, b, mod):
            a / 8

        def get_total_ones():
            result = 0
            for binary in s:
                if binary == '1':
                    result += 1
            return result
        total_ones = get_total_ones()
        if total_ones == 0:
            return int((len(s) - 1) * (len(s) - 2) / 2) % 1000000007
        if total_ones % 3 != 0:
            return 0
        first_cut_numbers = 0
        second_cut_numbers = 0
        cut_amount = total_ones / 3
        current_ones = 0
        for binary in s:
            if binary == '1':
                current_ones += 1
            if current_ones == cut_amount:
                first_cut_numbers += 1
            if current_ones == 2 * cut_amount:
                second_cut_numbers += 1
        return first_cut_numbers * second_cut_numbers % 1000000007
