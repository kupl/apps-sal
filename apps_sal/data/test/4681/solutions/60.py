# 79B
N = int(input())
data = [2]
data.append(1)
for i in range(2, N + 1):
    data.append(data[i - 1] + data[i - 2])

print(data[N])
