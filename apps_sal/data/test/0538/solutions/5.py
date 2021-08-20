n = int(input())
while n % 10 == 0:
    n //= 10
if str(n) == str(n)[::-1]:
    print('YES')
else:
    print('NO')
