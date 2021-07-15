N = int(input())
S = [input() for _ in range(2)]

types = []
i = 0
while i < N:
  if S[0][i] == S[1][i]:
    types.append(1)
    i += 1
  else:
    types.append(2)
    i += 2
MOD = 10**9 + 7
if types[0] == 1:
  ans = 3
else:
  ans = 6
for i in range(1,len(types)):
  if types[i] == 1 and types[i-1] == 1:
    ans *= 2
  elif types[i] == 1 and types[i-1] == 2:
    ans *= 1
  elif types[i] == 2 and types[i-1] == 1:
    ans *= 2
  elif types[i] == 2 and types[i-1] == 2:
    ans *= 3
  ans %= MOD
print((ans % MOD))
  

