n = int(input())
f = list(map(int, input().split()))
a = [None] * n
for i in range(n):
    a[f[i] - 1] = i
ans = sum(abs(a[i] - a[i - 1]) for i in range(1, n))
print(ans)
