(N, M) = list(map(int, input().split()))
if N <= M / 2:
    ans = N + (M - 2 * N) // 4
else:
    ans = M // 2
print(ans)
