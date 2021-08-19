class Solution:

    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        count = 0
        length = 1
        n_str = str(n)
        while length < len(n_str):
            count += len(digits) ** length
            length += 1
        digits_sorted = sorted(digits)
        current_digit = 0
        while current_digit < length:
            for digit in digits_sorted:
                next_round = False
                if digit < n_str[current_digit]:
                    count += len(digits) ** (length - current_digit - 1)
                elif digit > n_str[current_digit]:
                    return count
                elif current_digit == length - 1:
                    return count + 1
                else:
                    current_digit += 1
                    next_round = True
                    break
            if not next_round:
                return count
        return count
