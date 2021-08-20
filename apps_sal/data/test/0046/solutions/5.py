(n, m) = list(map(int, input().split()))
n5 = [0] * 5
for i in range(1, n + 1):
    n5[i % 5] += 1
m5 = [0] * 5
for i in range(1, m + 1):
    m5[i % 5] += 1
print(n5[0] * m5[0] + n5[1] * m5[4] + n5[2] * m5[3] + n5[3] * m5[2] + n5[4] * m5[1])
