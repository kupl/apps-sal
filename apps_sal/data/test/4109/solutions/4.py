N, M, X = list(map(int, input().split()))
C = []
D = []
for _ in range(N):
    line = list(map(int, input().split()))
    C.append(line[0])
    D.append(line[1:])

res = []
ans = []
for i in range(2 ** N):
    score = [0 for _ in range(M)]
    price = 0
    for j in range(N):
        if ((i >> j) & 1):
            price += C[j]
            for d in range(M):
                score[d - 1] += D[j][d]
    ifPassed = 1
    for m in range(M):
        if not score[m] >= X:
            ifPassed = 0
            break
    if ifPassed:
        ans.append(price)
if not ans:
    print((-1))
else:
    print((min(ans)))
