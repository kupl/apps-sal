n = int(input())
mod = 10**9+7
s1 = input()
s2 = input()

if s1[0] == s2[0]:
  i = 1
  ans = 3
  bef = "x"
else:
  i = 2
  ans = 6
  bef = "y"
while True:
  if i == n :
    break
  if s1[i] == s2[i]:
    if bef == "x":
      ans *= 2
    if bef == "y":
      ans *= 1
    i += 1
    bef = "x"
  else:
    if bef == "x":
      ans *= 2
    if bef == "y":
      ans *= 3
    i += 2
    bef = "y"
  ans %= mod
print((ans%mod))

