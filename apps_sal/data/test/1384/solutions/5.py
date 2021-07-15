n =  int(input())
data = list(map(int, input().split()))
data2 = [0] * n
data2[0] = data[0]
for i in range(1, n):
    if data[i]:
        data2[i] = data2[i - 1] + 1
    else:
        data2[i] = data2[i - 1]
data2 = [0] + data2
ma = -2
for i in range(n + 1):
    ma = max(ma, data2[-1] - data2[i] + i - data2[i])
print(ma)
