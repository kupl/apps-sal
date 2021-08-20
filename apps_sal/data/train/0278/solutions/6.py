class Solution:

    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits = collections.Counter(digits)
        final_ans_digits = {i: 0 for i in range(10)}
        for i in range(0, 10, 3):
            final_ans_digits[i] = digits[i]
        left_numbers = list()
        for i in [1, 2, 4, 5, 7, 8]:
            if digits[i] > 3:
                undefined = 3 + digits[i] % 3
                left_numbers += [i] * undefined
            else:
                left_numbers += [i] * digits[i]
        mod = sum(left_numbers) % 3
        if not mod:
            pass
        elif not (left_numbers[0] - mod) % 3:
            digits[left_numbers[0]] -= 1
        else:
            num1 = None
            for n in left_numbers:
                if not (n - mod) % 3:
                    num1 = n
                    digits[n] -= 1
                    break
            if num1 is None:
                num2 = None
                for i in range(1, len(left_numbers)):
                    if not (left_numbers[i] + left_numbers[0] - mod) % 3:
                        num2 = left_numbers[i]
                        digits[left_numbers[0]] -= 1
                        digits[num2] -= 1
                if num2 is None:
                    return ''
        ans = ''.join((str(i) * digits[i] for i in range(9, -1, -1)))
        if not ans:
            return ''
        elif ans[0] == '0':
            return '0'
        else:
            return ans
