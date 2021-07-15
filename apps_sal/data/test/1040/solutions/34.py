N=int(input())
S=input()
T=""
for s in S:
  T+=s
  if T[len(T)-3:len(T)]=="fox":
    T=T[:len(T)-3]
print(len(T))
