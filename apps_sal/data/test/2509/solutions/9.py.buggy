N, K = map(int, input().split())

if not K:
    print(N**2)
    return

ans = 0

for b in range(1, N + 1):
    if b - 1 < K:
        continue

    _before = N // b
    _before_n = b - K
    ans += _before * _before_n

    _after = N % b
    if _after + 1 < K:
        continue

    ans += _after - K + 1

print(ans)
