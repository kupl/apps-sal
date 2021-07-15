N=int(input())
S=input()

if N%2==1:
  print("No")
  return
if N%2==0:
  T_1=S[:(N//2)]
  T_2=S[N//2:]
  if T_1==T_2:
    print("Yes")
  else:
    print("No")
