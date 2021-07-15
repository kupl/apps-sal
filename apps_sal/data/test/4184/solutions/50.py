N = int(input())
W = list(map(int, input().split()))
 
# O(N^2)で解いても間に合う
m = 10**10
for i in range(1, N):
  a, b = 0, 0
  for j in range(i):
    a += W[j]
  for j in range(i, N):
    b += W[j]
  m = min(m, abs(a-b))
print(m)
