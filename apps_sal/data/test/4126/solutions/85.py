S=input()
N=len(S)
S_1=S[:int((N-1)//2)]
S_2=S[int((N+2)//2):]

if S==S[::-1] and S_1==S_1[::-1] and S_2==S_2[::-1]:
  print("Yes")
else:
  print("No")
