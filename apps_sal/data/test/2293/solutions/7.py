M, N = list(map(int, input().split()))
X = []
for i in range(M):
    X.append(set(list(map(int, input().split()))[1:]))

flg = 1
for i in range(M):
    for j in range(i):
        if len(X[i] & X[j]) == 0:
            flg = 0
            break
    if flg == 0:
        break

if flg:
    print("possible")
else:
    print("impossible")

