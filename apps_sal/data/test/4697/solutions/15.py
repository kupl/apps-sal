N, M = map(int, input().split())
if 2*N < M:
    extra = (M - 2*N) // 4
    ans = N + extra
else:
    ans = M // 2
print(ans)
