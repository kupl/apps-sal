class Solution:

    def maxDiff(self, num: int) -> int:
        num = [int(c) for c in str(num)]
        (max_num, min_num) = (num[:], num[:])
        for v in num:
            if v < 9:
                max_num = [digit if digit != v else 9 for digit in num]
                break
        if num[0] != 1:
            min_num = [digit if digit != num[0] else 1 for digit in num]
        else:
            for v in num[1:]:
                if v > 1:
                    min_num = [digit if digit != v else 0 for digit in num]
                    break
        print((max_num, min_num))
        return int(''.join([str(digit) for digit in max_num])) - int(''.join([str(digit) for digit in min_num]))
