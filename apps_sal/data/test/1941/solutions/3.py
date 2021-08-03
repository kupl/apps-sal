import math
A, B, n = map(int, input().split())
ans = []

for _ in range(n):
    l, t, m = map(int, input().split())

    if A + B * (l - 1) > t:
        ans.append(-1)
        continue

    r1 = (t - A) / B + 1
    D = (B - 2 * A) * (B - 2 * A) - 4 * B * (-2 * l * A + 2 * A - B * (l - 2) * (l - 1) - 2 * m * t)
    r2 = int(((B - 2 * A) + math.sqrt(D)) / 2 / B)

    if r1 > r2:
        r1 = r2
    ans.append(int(r1))


print("\n".join(map(str, ans)))
