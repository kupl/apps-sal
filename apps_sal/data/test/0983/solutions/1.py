(n, p, q, r) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
mx1 = [0] * n
mx1[0] = p * a[0]
for i in range(1, n):
    mx1[i] = max(p * a[i], mx1[i - 1])
mx2 = [0] * n
mx2[n - 1] = r * a[n - 1]
for i in range(n - 2, -1, -1):
    mx2[i] = max(r * a[i], mx2[i + 1])
ans = mx1[0] + q * a[0] + mx2[0]
for i in range(1, n):
    ans = max(ans, q * a[i] + mx1[i] + mx2[i])
print(ans)
