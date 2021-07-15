N,M = map(int,input().split())
X = sorted(list(map(int,input().split())))
L = []
for i in range(1,M):
    L.append(X[i]-X[i-1])
L = sorted(L,reverse=True)
if N>=M:
    print(0)
else:
    print(sum(L[N-1:]))
