N=int(input())
b = 0
a = list(map(int, input().split()))
c = 0
for i in range(0,N):
  c = c + a[i]
for i in range(0,N):
  c = c - a[i]
  b = (b + a[i] * c) %(10**9+7)
print(b)
