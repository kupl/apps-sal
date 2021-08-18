N, M = map(int, input().split())
Q = [tuple(map(int, input().split())) for _ in range(M)]

Q = sorted(Q, key=lambda x: x[1])
border = -1
ans = 0

for a, b in Q:
    if border <= a:
        ans += 1
        border = b

print(ans)
