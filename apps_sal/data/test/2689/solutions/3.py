a = list(input())
pre = []
i = 0
ans = ''
while i < len(a):
    if ord(a[i]) >= 48 and ord(a[i]) < 58 and (i < len(a)) and ('-' in a[i:]) and (a[i + 1] == '+'):
        b = a[i + 1:]
        p1 = b.index('-')
        ans += ''.join(a[i + 2:p1 + i + 1]) * int(a[i])
        i = i + p1 + 1
    elif a[i] != '+' and a[i] != '-' and (not (ord(a[i]) >= 48 and ord(a[i]) < 58)):
        ans += a[i]
    i += 1
print('Continue' if ans != ans[::-1] else 'Return')
