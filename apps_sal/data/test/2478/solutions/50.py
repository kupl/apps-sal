N=int(input())
S=input()

def add1(S):
  cum=[0]
  for i in range(len(S)):
    if S[i]=='(':cum.append(cum[-1]+1)
    else:cum.append(cum[-1]-1)
  if min(cum)>=0:return S
  out = '('*(-min(cum))
  out += S
  return out

def add2(S):
  cum=[0]
  for i in range(len(S)):
    if S[i]=='(':cum.append(cum[-1]+1)
    else:cum.append(cum[-1]-1)
      
  if cum[-1]==0:return S
  n = cum[-1]
  out = S + ')'*n
  return out

S = add1(S)
S = add2(S)
print(S)
