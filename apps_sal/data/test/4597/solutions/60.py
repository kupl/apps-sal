N = int(input())

K = 10**9 + 7
power = 1
for i in range(1, N+1):
  power = power%K
  power *= i

print(power%K)
