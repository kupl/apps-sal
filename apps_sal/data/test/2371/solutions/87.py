(n, z, w) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = abs(a[-1] - w)
if n > 1:
    ans = max(ans, abs(a[-2] - a[-1]))
print(ans)
