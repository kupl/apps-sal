from itertools import product
(N, M) = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(N)]


def f(score):
    return sum([score[i] * (-1) ** (1 - p[i]) for i in range(3)])


ans = 0
for p in product(range(2), repeat=3):
    s = list(map(f, scores))
    s = sorted(s, reverse=True)
    SUM = sum(s[:M])
    if ans < SUM:
        ans = SUM
print(ans)
