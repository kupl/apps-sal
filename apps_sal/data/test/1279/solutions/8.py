n, m = map(int, input().split())
a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
cnt = 0
cnt1 = 0
for i in range(n):
    if a[i] % 2 == 0:
        cnt += 1
for i in range(m):
    if b[i] % 2 == 0:
        cnt1 += 1
print(min(cnt, m - cnt1) + min(cnt1, n - cnt))
