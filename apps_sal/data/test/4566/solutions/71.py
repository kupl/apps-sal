n, m = map(int, input().split())
N = list(range(1, n + 1))
D = dict.fromkeys(N, 0)

for _ in range(m):
    R = list(map(int, input().split()))
    for r in R:
        D[r] += 1

for d in D.values():
    print(d)
