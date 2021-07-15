x = int(input())
while x % 10 == 0:
    x //= 10
x = str(x)
if x == x[::-1]:
    print('YES')
else:
    print('NO')
