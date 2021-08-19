(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = -1
ca = 0
cb = 0
for i in range(n):
    ca += a[i]
    c = min(ca, 8)
    ca -= c
    cb += c
    if k <= cb:
        ans = i + 1
        break
print(ans)
