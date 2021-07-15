N,*S = list(map(int,open(0).read().split()))

ans =sum(S)
if ans%10 !=0:
  print(ans)
else:
  S = sorted(S)
  for s in S:
    if s%10 != 0:
      print((ans-s))
      return
  print((0))

