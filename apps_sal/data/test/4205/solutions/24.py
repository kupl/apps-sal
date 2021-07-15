n = int(input())
p = list(map(int, input().split()))
a = sorted(p)
b = 0
for i in range(n):
    if p[i] != a[i]:
        b += 1
if b == 2 or b == 0:
    print('YES')
else:
    print('NO')
