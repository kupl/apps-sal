n = input()
while n[-1] == '0':
    n = n[:-1]
if n == n[::-1]:
    print('YES')
else:
    print('NO')
