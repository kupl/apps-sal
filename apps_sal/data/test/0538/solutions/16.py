x = int(input())
while x % 10 == 0:
    x //= 10
if list(str(x)) == list(reversed(str(x))):
    print('YES')
else:
    print('NO')
