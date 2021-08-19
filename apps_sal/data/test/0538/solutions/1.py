a = input()
for i in range(11):
    s = '0' * i + a
    if s == s[::-1]:
        print('YES')
        break
else:
    print('NO')
