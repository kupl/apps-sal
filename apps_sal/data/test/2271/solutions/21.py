n = int(input())
d = [0] * (n + 1)
for _ in range(n - 1):
  x, y = list(map(int, input().split()))
  d[x] += 1
  d[y] += 1
s = 0
for x in range(1, n + 1):
  s += d[x] * (d[x] - 1)
print(s // 2)

