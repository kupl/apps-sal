(N, M) = map(int, input().split())
n = N
m = M // 2
ans = 0
if n >= m:
    ans += m
else:
    ans += n
    m -= n
    ans += m // 2
print(ans)
