import sys
input = sys.stdin.readline
n,C = map(int,input().split())
ch = [[] for _ in range(C)]
tmax = 0
for _ in range(n):
  s,t,c = map(int,input().split())
  ch[c-1].append((s,t))
  tmax = max(tmax,t)
ch = [sorted(i,key= lambda x:x[0]) for i in ch]
imos = [0]*(tmax+2)
for i in ch:
  now = -1
  for ds,dt in i:
    if ds == now:
      imos[ds] +=1
    else:
      imos[ds-1] += 1
    imos[dt] -= 1
    now = dt
for i in range(tmax +1):
  imos[i+1] += imos[i]
print(max(imos))
