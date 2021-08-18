
import math


def reverse_sign(sign):
    if sign == '>=':
        return '<'
    elif sign == '<=':
        return '>'
    elif sign == '>':
        return '<='
    else:
        return '>='


N = int(input())
mn = int(-1.5 * math.pow(10, 9))
mx = int(1.5 * math.pow(10, 9))
for n in range(N):
    (sign, num, flag) = input().split()
    num = int(num)
    if flag == 'N':
        sign = reverse_sign(sign)

    if sign == '>':
        num += 1
        sign = '>='
    if sign == '<':
        num -= 1
        sign = '<='

    if sign == '>=':
        mn = max(mn, num)
    elif sign == '<=':
        mx = min(mx, num)

if mn > mx:
    print('Impossible')
else:
    print(mn)
