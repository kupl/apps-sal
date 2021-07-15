n = int(input())
v = sorted([int(i) for i in input().split()], reverse=True)
for i in range(n - 1):
  v[i] /= (2 ** (i + 1))
v[n-1] /= (2 ** (n - 1))
print(sum(v))
