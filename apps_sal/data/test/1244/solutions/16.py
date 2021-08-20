n = int(input())
q = [0] * 1005
f = 1
a = list(map(int, input().split()))
for i in range(n):
    q[a[i]] += 1
    if q[a[i]] > n // 2 + n % 2:
        f = 0
if f:
    print('YES')
else:
    print('NO')
