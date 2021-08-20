(n, m, k) = map(int, input().split())
a = list(map(int, input().split()))
mx1 = mx2 = 0
for i in range(n):
    if a[i] > mx1:
        mx2 = mx1
        mx1 = a[i]
    elif a[i] > mx2:
        mx2 = a[i]
t = m // (k + 1)
ans = t * k * mx1 + t * mx2
ans += m % (k + 1) * mx1
print(ans)
