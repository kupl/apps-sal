L = int(input())
def digits_count(n):
  cnt = 0
  while n != 0:
    cnt += 1
    n //= 2
  return cnt
def doubling(n, m):
  y = 1
  base = n
  while m != 0:
    if m % 2 == 1:
      y *= base
    base *= base
    m //= 2
  return y
m = digits_count(L)
A = [0 for _ in range(m)]
for i in range(m, 0, -1):
  A[i-1] = L % 2
  L //= 2
binomial = [1 for _ in range(m)]
for i in range(1, m):
  binomial[i] = binomial[i-1] * 2
vert = [[i*m+i+1, binomial[i]] for i in range(m-1)]
vert = vert[:] + [[i*m+i+1, 0] for i in range(m-1)]
S = doubling(2, m - 1)
for i in range(1, m):
  if A[i] == 1:
    vert.append([(m-i-1)*m+m-1, S])
    S += binomial[m-i-1]
print(m, len(vert))
for i in vert:
  print(i[0] // m + 1, i[0] % m + 1, i[1])
