class Solution:
    def getEnglishThousand(self, n):
        if 1 <= n <= 9:
            return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][n - 1]
        elif 10 <= n <= 19:
            return ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'][n - 10]
        elif 20 <= n <= 99:
            eng = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'][(n // 10) - 2]
            if n % 10 > 0:
                return eng + ' ' + self.getEnglishThousand(n % 10)
            else:
                return eng
        else:
            hundred = self.getEnglishThousand(n // 100) + ' Hundred'
            if n % 100 > 0:
                return hundred + ' ' + self.getEnglishThousand(n % 100)
            else:
                return hundred

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        stack = ['Billion', 'Million', 'Thousand', None]
        english = []
        while num:
            quantifier = stack.pop()
            if num % 1000 > 0:
                english.append(self.getEnglishThousand(num % 1000) + (' ' + quantifier if quantifier else ''))
            num //= 1000
        return ' '.join(reversed(english))
