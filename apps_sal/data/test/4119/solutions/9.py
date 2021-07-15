N, M = list(map(int ,input().split()))
X = list(map(int, input().split()))

X.sort()

subs = []
for i in range(M-1):
    subs.append(X[i+1]-X[i])
subs.sort()
if N == 1:
    print((sum(subs)))
    return
print((sum(subs[:-(N-1)])))

