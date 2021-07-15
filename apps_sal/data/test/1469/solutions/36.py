import math
L = int(input())
r = math.floor(math.log2(L))
N = r+1
graph = []
for i in range(1,r+1):
    graph.append([i,i+1,0])
    graph.append([i,i+1,2**(i-1)])
for t in range(N-1,0,-1):
    if L-2**(t-1) >= 2**r:
        graph.append([t,N,L-2**(t-1)])
        L -= 2**(t-1)

print((N,len(graph)))
for g in graph:
    print((*g))

