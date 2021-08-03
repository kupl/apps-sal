class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        # special case 0
        def translate(num):
            if num == 0:
                return ''
            less20 = [
                '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
            ]

            more20 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

            res = ''
            if num // 100:
                res = less20[num // 100] + ' Hundred' + (' ' if num % 100 else '')

            num %= 100
            res += less20[num] if num < 20 else more20[num // 10] + (' ' + less20[num % 10] if num % 10 else '')
            return res

        if num == 0:
            return 'Zero'

        unit = ['', 'Thousand', 'Million', 'Billion']
        i = 0
        res = []
        while num > 0:
            t = translate(num % 1000)
            if t:
                res += [unit[i], t]
            num //= 1000
            i += 1

        return (' '.join(res[::-1])).strip()
