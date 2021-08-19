# 2段目の文字列を逆にして1段目の文字列と一致すればいい
c = input('')
d = input('')

if c == d[::-1]:
    print('YES')
else:
    print('NO')
