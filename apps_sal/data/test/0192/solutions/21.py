(n, m) = list(map(int, input().split()))
s = [m, m, m]
ans = 0
while s[0] < n:
    val = min(n, s[1] + s[2] - 1)
    s[0] = s[1]
    s[1] = s[2]
    s[2] = val
    ans += 1
print(ans)
