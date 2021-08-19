(N, K) = list(map(int, input().split()))
ans = 0
for ab in range(2, 2 * N + 1):
    cd = ab - K
    if not 2 <= cd <= 2 * N:
        continue
    ans += min(ab - 1, 2 * N - ab + 1) * min(cd - 1, 2 * N - cd + 1)
print(ans)
