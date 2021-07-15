mod = 1000000007
n = int(input())
s = [ input() for i in range(2)]
ans = 1
i = 0
while i < n:
  if s[0][i] == s[1][i]:
    if i == 0:
      ans *= 3
    elif s[0][i-1] == s[1][i-1]:
      ans *= 2
    i += 1
  else:
    if i == 0:
      ans *= 6
    elif s[0][i-1] == s[1][i-1]:
      ans *= 2
    else:
      ans *= 3
    i+=2
  ans %= mod
print(ans)
