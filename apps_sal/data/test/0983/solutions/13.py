max1 = []
max2 = []
max3 = []
N, A, B, C = list(map(int, input().split()))
p = list(map(int, input().split()))
max1.append(-100000000000000000000)
max2.append(-100000000000000000000)
max3.append(-100000000000000000000)
for x in range(1, N + 1):
    max1.append(max(max1[x - 1], A * p[x - 1]))
for x in range(1, N + 1):
    max2.append(max(max2[x - 1], max1[x] + B * p[x - 1]))
for x in range(1, N + 1):
    max3.append(max(max3[x - 1], max2[x] + C * p[x - 1]))
print((max3[-1]))
