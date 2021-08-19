class Solution:

    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        current = 0
        for byte in data:
            b = '{0:08b}'.format(byte)
            if current == 0:
                cnt = 0
                for i in b:
                    if i == '0':
                        break
                    else:
                        cnt += 1
                if cnt == 1 or cnt > 4:
                    return False
                if cnt > 0:
                    current = cnt - 1
                else:
                    current = 0
            else:
                if b[0:2] != '10':
                    return False
                current -= 1
        if current > 0:
            return False
        return True
