n = input()
opr = len(n) - 1
cal_sum = 0
for i in range(2 ** opr):
    op = [''] * opr
    for j in range(opr):
        if i >> j & 1:
            op[opr - 1 - j] = '+'
    cal = ''
    for (x, y) in zip(n, op + ['']):
        cal += x + y
    cal_sum += eval(cal)
print(cal_sum)
