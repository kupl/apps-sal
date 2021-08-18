class Solution:
    def clumsy(self, N: int) -> int:
        temp = [i for i in range(N, 0, -1)]

        if N > 3:
            s = (temp[0] * temp[1] // temp[2] + temp[3])
            for i in range(1, N // 4):
                s -= (temp[i * 4] * temp[i * 4 + 1] // temp[i * 4 + 2] - temp[i * 4 + 3])
                print(s)
            if N % 4 == 3:
                s -= temp[-3] * temp[-2] // temp[-1]
            elif N % 4 == 2:
                s -= temp[-2] * temp[-1]
            elif N % 4 == 1:
                s -= temp[-1]

        else:
            s = 0
            if N % 4 == 3:
                s += temp[-3] * temp[-2] // temp[-1]
            elif N % 4 == 2:
                s += temp[-2] * temp[-1]
            elif N % 4 == 1:
                s += temp[-1]

        return s
