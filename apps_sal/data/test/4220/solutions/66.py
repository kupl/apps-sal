k=int(input())
s=list(input())
ss=("").join(s)
S=len(s)
sss=("").join(s[0:k])
if S<=k:
  print(ss)
else:
  print(sss+("..."))
