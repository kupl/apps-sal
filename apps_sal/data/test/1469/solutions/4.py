import math

L = int(input())
N = int(math.log2(L))+1

M = 2*(N-1)

# print(N, )
edges = []
for i in range(N-1):
    edges.append('{0} {1} {2}'.format((i+1) , (i+2), 0))
    
for i in range(N-1):
    edges.append('{0} {1} {2}'.format((i+1) , (i+2), 2**i))

node = L-2**(N-1)
X = 2**(N-1)

while node > 0:
    M += 1
    t = int(math.log2(node))+1
    edges.append('{0} {1} {2}'.format(t, N, X))
    node -= 2**(t-1)
    X += 2**(t-1)
    
output = """{0} {1}
{2}""".format(N,M,'\n'.join(edges))
print(output)
