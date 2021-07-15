n = int(input())
a = sorted(tuple(map(int, input().split())) for _ in range(n))
b = [x[1] for x in a]
for i in range(n - 1, 0, -1):
  b[i - 1] = min(b[i - 1], b[i])
for i in range(n - 1):
  if a[i][1] > b[i + 1]:
    print("Happy Alex")
    return
print("Poor Alex")
