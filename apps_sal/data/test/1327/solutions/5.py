from itertools import product as pr
n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in pr((-1, 1), repeat=3):
    li = sorted(l, key=lambda xf: sum(x * y for x, y in zip(i, xf)), reverse=1)[:m]
    ans = max(ans, sum(abs(sum(j)) for j in zip(*li)))
print(ans)
