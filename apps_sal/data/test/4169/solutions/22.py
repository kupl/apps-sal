N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[0])

ans = 0
bought = 0
for a, b in AB:
    m = min(M - bought, b)
    bought += m
    ans += a * m
print(ans)
