N = int(input())
S1 = list(input())
S2 = list(input())
MOD = 10**9 + 7

if S1[0] == S2[0]:
  ans = 3
  i = 1
else:
  ans = 6
  i = 2

while i < N:
  pre_s1, pre_s2 = S1[i-1], S2[i-1]
  s1, s2 = S1[i], S2[i]
  if pre_s1 == pre_s2:
    ans *= 2
    ans %= MOD
    if s1 == s2:
      i += 1
    else:
      i += 2
  else:
    if s1 == s2:
      i += 1
    else:
      ans *= 3
      ans %= MOD
      i += 2

print(ans)
