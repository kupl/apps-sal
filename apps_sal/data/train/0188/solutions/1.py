class Solution:

    def parseHundred(self, n):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        if n == 0:
            return ''
        w = ''
        while n > 0:
            if n > 99:
                digit = n // 100
                w += to19[digit - 1] + ' ' + 'Hundred'
                n = n % 100
                if n != 0:
                    w += ' '
            elif n <= 19:
                w += to19[n - 1]
                n = 0
            else:
                digit = n // 10
                w += tens[digit - 2]
                n = n % 10
                if n != 0:
                    w += ' '
        return w

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousands = ['', ' Thousand ', ' Million ', ' Billion ']
        i = 0
        w = ''
        if num == 0:
            return 'Zero'
        while num > 0:
            digits = num % 1000
            if digits != 0:
                w = self.parseHundred(digits) + thousands[i] + w
            num = num // 1000
            i += 1
        return w.strip()
