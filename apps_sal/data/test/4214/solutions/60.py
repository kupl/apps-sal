import itertools

N = int(input())
X = []
Y = []
seq = list(itertools.permutations([i for i in range(1,N+1)]))
a = 0
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
for h in range(len(seq)):
    for i in range(N-1):
        a += ((X[seq[h][i]-1]-X[seq[h][i+1]-1])**2+(Y[seq[h][i]-1]-Y[seq[h][i+1]-1])**2)**0.5
print(a/len(seq))
