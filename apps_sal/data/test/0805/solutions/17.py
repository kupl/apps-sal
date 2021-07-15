n = int(input())
a = [0] * 100
la, ra = map(int, input().split())
for i in range(1, n):
    l, r = map(int, input().split())
    a[l] += 1
    if r < 100:
        a[r] -= 1
for i in range(1, 100):
    a[i] += a[i - 1]
ans = 0
for i in range(la, ra):
    if a[i] == 0:
        ans += 1
print(ans)
