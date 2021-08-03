def dice_expectation(p):
    return ((1 + p) * p / 2) * (1 / p)


n, k = list(map(int, input().split()))
pp = [0] * (n + 1)
for i, p in enumerate(map(int, input().split())):
    pp[i + 1] = pp[i] + dice_expectation(p)

max = -1
for i in range(k, n + 1, 1):
    max = pp[i] - pp[i - k] if pp[i] - pp[i - k] > max else max

print(max)
