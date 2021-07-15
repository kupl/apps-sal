from sys import stdin, stdout

n, U = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

k = 0
ans = -1
for i in range(n):
    while k+1 < n and a[k+1] - a[i] <= U:
        k += 1
    if k - i < 2:
        continue
    j = i+1
    cur = (a[k] - a[j]) / (a[k] - a[i])
    ans = max(ans, cur)
print(ans)
