n = int(input())
a = list(map(int, input().split()))
max = 0
for i in range(n):
  for j in range(i+1, n):
    if abs(a[j] - a[i]) > max:
      max = abs(a[j] - a[i])
print(max)
