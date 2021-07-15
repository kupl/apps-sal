N, M = map(int, input().split())

ab = []
for _ in range(M):
    a, b = map(int, input().split())
    ab.append((a, b))
ab.sort(key=lambda ab: ab[::-1])

ans = 0
last = -1
for a, b in ab:
    if not a <= last < b:
        last = b - 1
        ans += 1
print(ans)
