N=int(input())
S="".join(input().split("fox"))
T=""
for s in S:
  T+=s
  if T[len(T)-3:len(T)]=="fox":
    T=T[:len(T)-3]
print(len(T))
