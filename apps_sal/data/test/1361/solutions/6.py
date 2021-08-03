n = int(input())
d = input()
d = [int(d) for d in d.split()]
m1 = -1
m = 10000000000
for i in range(0, n - 1):
    if d[i + 1] - d[i] > m1:
        m1 = d[i + 1] - d[i]
for i in range(1, n - 1):
    if d[i + 1] - d[i - 1] < m:
        m = d[i + 1] - d[i - 1]
print(max(m, m1))
