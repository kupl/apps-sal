k, a, b, v = list(map(int, input().split()))
for i in range(1, 2000):
    t = min(k, b + 1)
    a -= t * v
    b -= t - 1
    if a <= 0:
        print(i)
        break
