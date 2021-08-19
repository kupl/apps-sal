(N, M) = map(int, input().split())
ans = 0
if 2 * N >= M:
    ans = M // 2
else:
    ans += N
    C = M - 2 * N
    ans += C // 4
print(ans)
