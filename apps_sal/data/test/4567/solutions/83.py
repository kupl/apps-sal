N = int(input())
S = sorted([int(input()) for n in range(N)])
S1 = []
S2 = []

for s in S:
  if s%10 ==0:
    S1.append(s)
  else:
    S2.append(s)
    
if sum(S)%10!=0:
  print(sum(S))
else:
  if len(S2)>0:
    print(sum(S)-S2[0])
  else:
    print(0)
