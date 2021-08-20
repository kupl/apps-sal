class Solution:

    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        tot = 0
        b = bin(n)[2:]
        if b[1] == '0':
            tot += 2 ** (len(b) - 2)
        lastChanged = b[1] == '0'
        for i in range(2, len(b)):
            if lastChanged and b[i] == '0' or (not lastChanged and b[i] == '1'):
                tot += 2 ** (len(b) - 1 - i)
                lastChanged = True
            else:
                lastChanged = False
        return tot + 1 + self.minimumOneBitOperations(int('1' + '0' * (len(b) - 2), 2))
