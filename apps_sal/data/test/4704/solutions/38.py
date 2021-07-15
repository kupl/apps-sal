N = int(input())
a = list(map(int, input().split()))
sa = a[:]
for i in range(N-1):
  sa[i+1] += sa[i]

diff = float('inf')
for i in range(N-1):
  if abs(sa[i] - (sa[-1] - sa[i])) < diff:
    diff = abs(sa[i] - (sa[-1] - sa[i]))

print(diff)
