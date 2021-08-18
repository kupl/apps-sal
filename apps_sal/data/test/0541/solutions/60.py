from operator import itemgetter

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

cd = sorted(ab, key=itemgetter(1))
removed = -1
ans = 0

for a, b in cd:
    if a > removed:
        removed = b - 1
        ans += 1

print(ans)
