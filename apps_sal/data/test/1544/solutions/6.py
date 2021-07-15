def fact(i):
  ans = 1
  for j in range(1, i + 1):
    ans *= j
  return ans

def c(i, j):
  return fact(i + j - 1) // (fact(j) * fact(i - 1))

n = int(input())
print(c(n, 5) * c(n, 3))
