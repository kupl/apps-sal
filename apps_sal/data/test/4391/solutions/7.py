(n, k) = list(map(int, input().split()))
temps = [int(i) for i in input().split()]
predpr = [0]
for i in range(n):
    predpr.append(predpr[i] + temps[i])
ma = 0
for i in range(1, n - k + 2):
    for j in range(i + k - 1, n + 1):
        cur = (predpr[j] - predpr[i - 1]) / (j - i + 1)
        if cur > ma:
            ma = cur
print(ma)
