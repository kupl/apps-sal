def inverse(str):
    val = ''
    if str == '>':
        val = '<='
    elif str == '<':
        val = '>='
    elif str == '>=':
        val = '<'
    else:
        val = '>'
    return val


min_ = -2000000000
max_ = 2000000000
n = int(input())
for i in range(n):
    (sign, num, yn) = input().split()
    num = int(num)
    if yn == 'N':
        sign = inverse(sign)
    if sign == '<=':
        max_ = min(max_, num)
    elif sign == '<':
        max_ = min(max_, num - 1)
    elif sign == '>=':
        min_ = max(min_, num)
    else:
        min_ = max(min_, num + 1)
if min_ <= max_:
    print(min_)
else:
    print('Impossible')
