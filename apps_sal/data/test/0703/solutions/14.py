(k, a, b, v) = list(map(int, input().split()))
t = (a + v - 1) // v
for x in range(1, t + 1):
    if 0 <= t - x <= b and x <= t <= k * x:
        print(x)
        break
