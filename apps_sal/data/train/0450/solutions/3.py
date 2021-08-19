class Solution:

    def validUtf8(self, data):
        n = len(data)
        check10 = 0
        for byte in data:
            if check10:
                if byte & 192 != 128:
                    return False
                check10 -= 1
            elif byte & 248 == 240:
                check10 = 3
            elif byte & 240 == 224:
                check10 = 2
            elif byte & 224 == 192:
                check10 = 1
            elif byte & 128 == 0:
                continue
            else:
                return False
        return check10 == 0
