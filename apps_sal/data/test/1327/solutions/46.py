from itertools import product
(n, m) = list(map(int, input().split()))
xyz = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for subset in product((-1, 1), repeat=3):

    def func(xyz):
        return sum((x * a for (x, a) in zip(xyz, subset)))
    score = sum(sorted(map(func, xyz), reverse=True)[:m])
    if ans < score:
        ans = score
print(ans)
