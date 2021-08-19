class Solution:

    def validUtf8(self, data):
        seqs = len(data)
        idx = 0
        while idx < seqs:
            number = data[idx] & 255 | 256
            seq = bin(number)[3:]
            bits = len(seq.split('0')[0])
            if idx + bits > seqs:
                return False
            elif bits > 4:
                return False
            elif bits == 0:
                idx += 1
            elif bits == 1:
                return False
            else:
                for i in range(1, bits):
                    num = data[idx + i] & 255
                    if num >= int('11000000', 2) or num < int('10000000', 2):
                        return False
                idx += bits
        return True
