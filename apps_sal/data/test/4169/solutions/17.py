n, m = map(int, input().split())
a = []
cnt = 0
for i in range(n):
    k, j = input().split()

    a.append([int(k), int(j)])
a = sorted(a)
for i in range(n):
    if a[i][1] >= m:
        cnt += a[i][0] * m
        break
    else:
        cnt += a[i][0] * a[i][1]
        m -= a[i][1]
print(cnt)
