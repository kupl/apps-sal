R = lambda: list(map(int, input().split()))
n, m = R()
a = R()
b = R()
i = j = 0
while i < n and j < m:
  if b[j] < a[i]:
    j += 1
  else:
    i += 1
    j += 1
print(n - i)
