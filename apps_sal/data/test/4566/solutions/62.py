n, m = map(int, input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())

ans = [0] * n

for i in range(m):
    ans[a[i]-1] += 1
    ans [b[i]-1] += 1

for i in ans:
    print(i)
