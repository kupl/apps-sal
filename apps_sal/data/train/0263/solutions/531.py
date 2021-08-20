class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 0:
            return n
        pad = []
        for i in range(4):
            pad.append([1] * 3)
        pad[3][0] = 0
        pad[3][2] = 0
        for k in range(n - 1):
            newPad = []
            for i in range(4):
                newPad.append([1] * 3)
            newPad[0][0] = pad[1][2] + pad[2][1]
            newPad[0][1] = pad[2][0] + pad[2][2]
            newPad[0][2] = pad[1][0] + pad[2][1]
            newPad[1][0] = pad[0][2] + pad[2][2] + pad[3][1]
            newPad[1][1] = 0
            newPad[1][2] = pad[0][0] + pad[2][0] + pad[3][1]
            newPad[2][0] = pad[1][2] + pad[0][1]
            newPad[2][1] = pad[0][0] + pad[0][2]
            newPad[2][2] = pad[0][1] + pad[1][0]
            newPad[3][0] = 0
            newPad[3][1] = pad[1][0] + pad[1][2]
            newPad[3][2] = 0
            pad = newPad
        total = 0
        for i in range(len(pad)):
            total += sum(pad[i])
        return total % (10 ** 9 + 7)
