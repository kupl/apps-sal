r, d, x = map(int, input().split())
for alg in range(10):
    x *= r
    x -= d
    print(x)
