class Solution:

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = ''
        while int(num):
            digits += str(int(num % 10))
            num /= 10
        digits = digits[::-1]
        lens = len(digits)
        mark = 0
        mark1 = 0
        flag = 0
        for i in range(lens):
            maxs = ord(digits[i])
            for j in range(i + 1, lens, 1):
                if ord(digits[j]) >= maxs:
                    maxs = ord(digits[j])
                    mark = j
            if maxs != ord(digits[i]):
                mark1 = i
                flag = 1
                break
        digit = list(digits)
        if flag == 1:
            tem = digit[mark1]
            digit[mark1] = digit[mark]
            digit[mark] = tem
        res = 0
        for i in range(lens):
            res *= 10
            res += ord(digit[i]) - ord('0')
        return res
