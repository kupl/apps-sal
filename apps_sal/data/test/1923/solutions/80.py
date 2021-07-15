n = int(input())
a = sorted(list(map(int, input().split())))
s = 0
for i in range(2 * n):
  if i % 2 == 0:
    s += a[i]
print(s)
