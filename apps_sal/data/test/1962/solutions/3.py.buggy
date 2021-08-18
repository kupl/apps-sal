n, k, l = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))

p = 0
while p < len(a) and a[p] - a[0] <= l:
    p += 1

if p < n:
    print(0)
    return

ans = 0
u = 0
for i in range(n):
    ans += a[u]
    if u + k >= p - (n - i - 1):
        u = p - (n - i - 1)
    else:
        u += k
print(ans)
