n = int(input())
s = 1
ans = 1
for i in range(1, n+1):
  s *= i
for i in range(2, n+1):
  k = 1
  while s % i == 0:
    s = s // i
    k += 1
  ans *= k
print(ans % (10 ** 9 + 7))
