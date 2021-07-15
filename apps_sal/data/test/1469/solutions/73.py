#import math
L = int(input())
#r = math.floor(math.log2(L))
r = L.bit_length()-1
N = r+1
graph = []
append = graph.append
for i in range(1,r+1):
    append([i,i+1,0])
    append([i,i+1,2**(i-1)])

for t in range(N-1,0,-1):
    if L-2**(t-1) >= 2**r:
        append([t,N,L-2**(t-1)])
        L -= 2**(t-1)

print((N,len(graph)))
for g in graph:
    print((*g))

