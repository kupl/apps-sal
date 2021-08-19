class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        le = len(s) - 1
        max = 1
        for ma in range(pow(2, le) - 1, 0, -1):
            bi = format(ma, '0' + str(le) + 'b') + '1'
            prev = 0
            lis = []
            valid = True
            for bit in range(len(bi)):
                if bi[bit] == '1':
                    part = s[prev:bit + 1]
                    if part in lis:
                        valid = False
                        break
                    lis.append(part)
                    prev = bit + 1
            if valid and len(lis) > max:
                max = len(lis)
        return max
