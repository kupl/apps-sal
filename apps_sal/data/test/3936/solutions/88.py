N = int(input())
S1 = str(input())
S2 = str(input())

if S1[0] == S2[0]:
  ans = 3
  cnt = 1
  tmp = 0
else:
  ans = 6
  cnt = 2
  tmp = 1
  
while cnt < N:
  if tmp == 0:
    if S1[cnt] == S2[cnt]:
      ans *= 2
      cnt += 1
    else:
      ans *= 2
      cnt += 2
      tmp = 1
  else:
    if S1[cnt] == S2[cnt]:
      cnt += 1
      tmp = 0
    else:
      ans *= 3
      cnt += 2
print(ans%1000000007)
