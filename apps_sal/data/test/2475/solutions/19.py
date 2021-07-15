N = int(input())
*S, = map(int, input().split())

ans = 0
for d in range(1, N):
    r = k = 0
    while k*d <= N-1:
        a = N-1-k*d
        if a <= d or (a <= k*d and a % d == 0):
            break
        r += S[N-1-k*d] + S[k*d]
        k += 1
        ans = max(ans, r)
print(ans)
