n = int(input())
t = sorted(list(map(int, input().split())))
T = int(input())
ans = 0
l = 0
r = 0
while r < n:
    ans = max(ans, r - l + 1)
    if r == n - 1:
        break
    if t[r + 1] - t[l] <= T:
        r += 1
    else:
        l += 1
print(ans)
