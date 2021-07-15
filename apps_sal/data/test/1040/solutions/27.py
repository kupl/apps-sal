N=int(input())
S=input()
T=[]
n=0


for s in S:
  T.append(s)
  if T[-3:]==['f','o','x']:
    T.pop()
    T.pop()
    T.pop()
    n+=1
print(len(S)-3*n)
