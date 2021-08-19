import sys
(n, d) = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
res = 2
for i in range(len(x)):
    if i > 0 and abs(x[i] - d - x[i - 1]) >= d:
        res += 1
    if i < len(x) - 1 and abs(x[i] + d - x[i + 1]) > d:
        res += 1
print(res)
