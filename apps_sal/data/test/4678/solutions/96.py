import math


def cin():
    return list(map(int, input().split()))


N = int(input())
data = cin()
total = 0
for i in range(N - 1):
    if data[i + 1] < data[i]:
        total += data[i] - data[i + 1]
        data[i + 1] = data[i]
print(total)
