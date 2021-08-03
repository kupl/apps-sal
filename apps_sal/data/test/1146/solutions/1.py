n, m = list(map(int, input().split()))
p = [0] * m
for i in range(n):
    a = list(map(int, input().split()))
    for t in range(1, len(a)):
        p[a[t] - 1] = 1
if min(p) == 0:
    print('NO')
else:
    print('YES')
