class Solution:
    def validUtf8(self, data):
        seqs = len(data)
        idx = 0
        while idx < seqs:
            number = data[idx] & 255 | 256  # XXX: make it as 0b1xxxxxxxx
            seq = bin(number)[3:]
            bits = len(seq.split('0')[0])

            if idx + bits > seqs:
                return False
            elif bits > 4:
                # maximum 4 bytes
                # 0b11111111
                return False
            elif bits == 1:
                # 0b10000000
                return False
            elif bits == 0:
                # 1 byte UTF-8
                idx += 1
            else:
                for i in range(1, bits):
                    num = data[idx + i] & 255
                    if num >= int('11000000', 2) or num < int('10000000', 2):
                        return False
                idx += bits

        return True
