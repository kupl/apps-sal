N,K = map(int,input().split())
keta = 0
while N>0:
  N = N//K
  keta = keta + 1

print(keta)
