n = int(input())
a = list(map(int, input().split()))
t = 0
l = 0
r = 0
ans = 0
while r < n:
    if t ^ a[r] == t + a[r]:
        t += a[r]
        r += 1
    else:
        t -= a[l]
        ans += r - l
        l += 1
ans += (r - l) * (r - l + 1) // 2
print(ans)
