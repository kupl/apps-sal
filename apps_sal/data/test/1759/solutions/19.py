R = lambda:map(int, input().split())
m, n = R()
t = [0] * (n + 1)
c = []
for i in range(m):
  a = list(R())
  for j in range(n):
    t[j + 1] = max(t[j], t[j + 1]) + a[j]
  c += [str(t[n])]
print(" ".join(c))
