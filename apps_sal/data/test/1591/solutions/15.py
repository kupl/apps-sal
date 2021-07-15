from math import ceil
n, k = list(map(int, input().split()))
a = []
for i in range(n):
  a.append(int(input()))
res = 0
d = [0] * 1024
for i in a:
  d[i] += 1
for i in d:
  res += 2 * (i // 2)
res = res + ceil((n - res) / 2)
print(res)

