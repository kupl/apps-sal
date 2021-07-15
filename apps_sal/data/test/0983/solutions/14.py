inf = 10 ** 18
n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
mx = [-inf] * n
mn = [inf] * n
val2 = [0] * n
mx[0] = a[0]
mn[0] = a[0]
val2[0] = p * a[0] + q * a[0]
for i in range(1, n):
    mn[i] = min(mn[i - 1], a[i])
    mx[i] = max(mx[i - 1], a[i])
    val2[i] = q * a[i] + max(mn[i] * p, mx[i] * p)
val3 = [0] * n
mx2 = [-inf] * n
mx2[0] = val2[0]
val3[0] = val2[0] + r * a[0]
ans = - inf
for i in range(1, n):
    mx2[i] = max(mx2[i - 1], val2[i])
    val3[i] = r * a[i] + mx2[i]
print(max(val3))
