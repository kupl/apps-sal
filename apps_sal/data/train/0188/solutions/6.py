class Solution:

    digit = {
        0: '',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }

    teen = {
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen'
    }

    ten = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }

    idx = {
        0: '',
        1: 'Thousand',
        2: 'Million',
        3: 'Billion',
        4: 'Trillion',
        5: 'Quadrillion'
    }

    def helper(self, num):
        result = ""
        while len(num) < 3:
            num = '0' + num

        if num[0] is not '0':
            result = self.digit[int(num[0])] + ' Hundred'
        if num[1] is not '0':
            if num[1] == '1':
                return result + " " + self.teen[int(num[1] + num[2])]
            else:
                return result + " " + self.ten[int(num[1])] + " " + self.digit[int(num[2])]
        if num[2] is not '0':
            result = result + " " + self.digit[int(num[2])]
        return result

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        result = ""
        rev = str(num)[::-1]
        slices = [rev[i:i + 3] for i in range(0, len(str(num)), 3)]

        for idx, slice in enumerate((slices)):
            if slice == '000':
                continue
            else:
                result = self.helper(str(slice[::-1])) + " " + self.idx[idx] + " " + result
        result = result.split(' ')
        result = [x for x in result if x is not ""]
        return ' '.join(result)
