n = int(input())
ar = []
for i in range(n):
    a, b = [int(i) for i in input().split()]
    ar.append((a - b, a + b))
c = [[0, 0] for i in range(2001)]
for i in range(n):
    c[ar[i][0] + 999][0] += 1
    c[ar[i][1]][1] += 1
ct = 0
for i in range(2001):
    ct += (c[i][0] * (c[i][0] - 1) + c[i][1] * (c[i][1] - 1)) // 2
print(ct)
