N, K = map(int, input().split())
ans = 0


def func(k):
    return min(k - 1, 2 * N + 1 - k)


for i in range(2, 2 * N + 1):
    ab = i
    cd = ab - K
    # 2 <= cd <= 2*N
    if cd < 2 or cd > 2 * N:
        continue
    ans += func(ab) * func(cd)

print(ans)
