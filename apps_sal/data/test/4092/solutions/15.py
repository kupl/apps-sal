N, = list(map(int, input().split()))
X = list(map(int, input().split()))
#print(X)
for i in range(1, N):
    X[i] += X[i-1]
#print(X)
d = set([0])
R = 0
for i in range(N):
    if X[i] in d:
#        print(i)
        R += 1
        d = set()
    d.add(X[i])
    if i>0:
        d.add(X[i-1])
print(R)

