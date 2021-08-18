from operator import itemgetter

n, m = map(int, input().split())

ab = sorted([tuple(map(int, input().split())) for i in range(m)], key=itemgetter(1))
removed = -1
ans = 0

for a, b in ab:
    if a > removed:
        removed = b - 1
        ans += 1

print(ans)
