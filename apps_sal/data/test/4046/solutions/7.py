n = int(input())
q = list(map(int, input().split()))
a = [0 for i in range(n)]
for i in range(n - 1):
    a[i + 1] = q[i] + a[i]
mn = min(a)
for i in range(n):
    a[i] = a[i] - mn + 1
if len(set(a)) != n or max(a) > n:
    print(-1)
else:
    print(*a)
