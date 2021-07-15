n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(n):
  for j in range(i + 1, n):
    s += a[i] * a[j]
print(s)
