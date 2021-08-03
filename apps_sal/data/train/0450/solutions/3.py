class Solution:
    def validUtf8(self, data):
        n = len(data)
        check10 = 0
        for byte in data:
            if check10:
                if byte & 0b11000000 != 0b10000000:
                    return False
                check10 -= 1
            elif byte & 0b11111000 == 0b11110000:
                check10 = 3
            elif byte & 0b11110000 == 0b11100000:
                check10 = 2
            elif byte & 0b11100000 == 0b11000000:
                check10 = 1
            elif byte & 0b10000000 == 0:
                continue
            else:
                return False
        return check10 == 0
