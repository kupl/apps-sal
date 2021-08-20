(N, K) = map(int, input().split())
s = N // K
t = N % K
ans = s ** 3
if K % 2 == 0:
    u = K // 2
    if t < u:
        ans += s ** 3
    else:
        ans += (s + 1) ** 3
print(ans)
