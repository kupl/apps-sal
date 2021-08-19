(n, x) = input().split()
n = int(n)
x = int(x)
sum = 0
for i in input().split():
    sum += int(i)
if sum + n - 1 != x:
    print('NO')
else:
    print('YES')
