N,K = map(int,input().split())
p = list(map(int,input().split()))
sp = sorted(p)
goukei = 0

for i in range(K):
  goukei += sp[i]

print(goukei)
