a_3_3 = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b_n = [int(input()) for _ in range(n)]


class Info:

    def __init__(self, a_3_3, n, b_n):
        self.a_3_3 = a_3_3
        self.n = n
        self.b_n = b_n

    @staticmethod
    def setting():
        for num in b_n:
            for line in a_3_3:
                if num in line:
                    line[line.index(num)] = 0
        return a_3_3

    @staticmethod
    def result():
        diagonal_lurd = a_3_3[0][0] + a_3_3[1][1] + a_3_3[2][2]
        diagonal_ldru = a_3_3[2][0] + a_3_3[1][1] + a_3_3[0][2]
        for (index, line) in enumerate(a_3_3):
            row_sum = sum(line)
            col_sum = a_3_3[0][index] + a_3_3[1][index] + a_3_3[2][index]
            if diagonal_lurd == 0 or diagonal_ldru == 0 or row_sum == 0 or (col_sum == 0):
                print('Yes')
                return
        print('No')


info = Info(a_3_3, n, b_n)
info.setting()
info.result()
