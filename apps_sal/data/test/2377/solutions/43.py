import math

n, h = map(int, input().split())
ab = [None] * n
for i in range(n):
    ab[i] = tuple(map(int, input().split()))

amax = max([m[0] for m in ab])

ans = 0
for a, b in sorted(ab, key=lambda m: -m[1]):
    if b <= amax:
        break
    h -= b
    ans += 1
    if h <= 0:
        print(ans)
        return

ans += math.ceil(h / amax)
print(ans)
