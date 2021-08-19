import math
a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = int(input())
x = math.ceil(sum(a) / 5)
y = math.ceil(sum(b) / 10)
if x + y <= n:
    print('YES')
else:
    print('NO')
