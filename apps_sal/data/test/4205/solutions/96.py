n = int(input())
l = list(range(1, n + 1))
p = list(map(int, input().split()))
m = 0
for i in range(n):
    if p[i] != l[i]:
        m += 1
if m >= 3:
    print('NO')
else:
    print('YES')
