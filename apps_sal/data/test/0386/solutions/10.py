n = int(input())
mn = -2000000000
mx = 2000000000
for i in range(n):
    (sign, ber, ans) = input().split()
    num = int(ber)
    if ans == 'N':
        if sign == '<':
            sign = '>='
        elif sign == '<=':
            sign = '>'
        elif sign == '>':
            sign = '<='
        elif sign == '>=':
            sign = '<'
    if sign == '<':
        sign = '<='
        num -= 1
    if sign == '>':
        sign = '>='
        num += 1
    if sign == '<=':
        mx = min(mx, num)
    else:
        mn = max(mn, num)
if mx < mn:
    print('Impossible')
else:
    print(mn)
