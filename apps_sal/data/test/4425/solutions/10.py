(n, k) = list(map(int, input().split()))
rate = 0
for i in range(1, n + 1):
    score = i
    prob = 1 / n
    while score < k:
        score *= 2
        prob /= 2
    rate += prob
print(rate)
