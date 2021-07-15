n = int(input())
a = list(map(int, input().split()))

N = 100001
d = [-1] * N
p = [-1] * N
for i in range(n):
  if p[a[i]] == -1:
    d[a[i]] = 0
  else:
    if i - p[a[i]] != d[a[i]]:
      if d[a[i]] == 0:
        d[a[i]] = i - p[a[i]]
      else:
        d[a[i]] = -1
  p[a[i]] = i

count = 0
for i in range(N):
  if d[i] != -1:
    count += 1
print(count)
print('\n'.join("{0} {1}".format(i, d[i]) for i in range(N) if d[i] != -1))
