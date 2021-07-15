from sys import stdout
import heapq
printn = lambda x: stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      list(map(int, input().split()))
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def setc2c():
  for c1 in range(n):
    dist = [BIG]*n
    dist[c1] = 0
    hp = [(0,c1)]
    while len(hp)>0:
        curlen,curloc = heapq.heappop(hp)
        if curlen > dist[curloc]:
            continue
        for nxtloc in dst[curloc]:
            newdist = dist[curloc]+1
            if newdist < dist[nxtloc]:
                dist[nxtloc] = newdist
                heapq.heappush(hp, (newdist, nxtloc))
    for c2 in range(n):
        c2c[c1][c2] = dist[c2]

# main

n = inn()
dst = [ [] for i in range(n) ]
c2c = [ [0]*n for i in range(n) ]

for i in range(n):
    s = input()
    for j in range(n):
        if s[j]=='1':
            dst[i].append(j)

m= inn()
p = [x-1 for x in inl()]

setc2c()

v = [p[0]]
curv = p[0]
curi = 0
for i in range(1,m):
    if c2c[curv][p[i]] < i - curi:
        v.append(p[i-1])
        curv = p[i-1]
        curi = i-1

v.append(p[m-1])
k = len(v)
print(k)
for i in range(k):
    printn((' ' if i>0 else '') + str(v[i]+1))
print('')

