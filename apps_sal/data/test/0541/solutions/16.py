from operator import itemgetter
(N, M) = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]
ab = sorted(ab, key=itemgetter(1))
removed = -1
ans = 0
for (a, b) in ab:
    if a > removed:
        removed = b - 1
        ans += 1
print(ans)
