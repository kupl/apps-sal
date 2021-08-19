s = input()
n = 10
while n and s != s[::-1]:
    s = '0' + s
    n -= 1
if n == 0:
    print('NO')
else:
    print('YES')
