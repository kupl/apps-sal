n = int(input())
data = sorted(list(map(int, input().split())))
min1 = 10 ** 9 + 1
for i in range(n):
    data[i] = min(data[i], i + 1, min1)
    min1 = data[i] + 1
print(data[-1] + 1)
