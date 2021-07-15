from heapq import *
n,q = map(int,input().split())
kg = [[] for _ in range(2*10**5)]
pos = [0]*n
rate = [0]*n
for i in range(n):
    a,b = map(int,input().split())
    b-=1
    heappush(kg[b], (-a,i))
    pos[i] = b
    rate[i] = a

evenness = []
for i in range(2*10**5):
    if kg[i]:
        a,c = kg[i][0]
        heappush(evenness, (-a,c))

for _ in range(q):
    c,d = map(int,input().split())
    c,d = c-1,d-1
    prev = pos[c]
    pos[c] = d
    heappush(kg[d], (-rate[c],c))
    while kg[prev] and pos[kg[prev][0][1]]!=prev:
        heappop(kg[prev])
    while kg[d] and pos[kg[d][0][1]]!=d:
        heappop(kg[d])
    if kg[prev]:
        a,c = kg[prev][0]
        heappush(evenness, (-a,c))
    if kg[d]:
        a,c = kg[d][0]
        heappush(evenness, (-a,c))
    while evenness and kg[pos[evenness[0][1]]][0][1]!=evenness[0][1]:
        heappop(evenness)
    print(evenness[0][0])
