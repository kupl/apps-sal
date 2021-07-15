import numpy as np
N,A,B = list(map(int,input().split()))

if A+B > N+1:
  print("-1")
  return
if A == 1:
  if B== N:
    ans = [i+1 for i in reversed(list(range(N)))]
    print((*ans))
    return
  else:
    print("-1")
    return
if B == 1:
  if A== N:
    ans = [i+1 for i in range(N)]
    print((*ans))
    return
  else:
    print("-1")
    return
if A >= B:
  Flag = True
else:
  Flag = False
  A,B = B,A
#print((N+A-1)//A, B)
if A*B<N:
  print("-1")
  return
else:
  L = [1 for _ in range(B)]
  nokori = N-B
  for i in range(B):
    if A-L[i] >0:
      temp = min(A-L[i],nokori)
      L[i] += temp
      nokori -= temp
    if nokori == 0:
      break
  now = 0
  P = [[] for _ in range(B)]
  for i,num in enumerate(L):
    for j in range(num):
      now += 1
      P[-i-1].append(now)
  #print(P)
  ans = P
  output = []
  for i in range(len(ans)):
    for j in ans[i]:
      output.append(j)
  if Flag:
    print((*output))
  else:
    output = output[::-1]
    print((*output))

