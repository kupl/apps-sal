(N, K) = map(int, input().split())
A = sorted(list(map(int, input().split())))[::-1]
S = 0
ans = 0
for a in A:
    if S + a < K:
        S += a
        ans += 1
    else:
        ans = 0
print(ans)
