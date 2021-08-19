N = int(input())
T = list(map(int, input().split()))
M = int(input())
L = []
res = []
for i in range(M):
    (P, X) = list(map(int, input().split()))
    buf = []
    for j in range(len(T)):
        if P == j + 1:
            buf.append(X)
        else:
            buf.append(T[j])
    res.append(sum(buf))
for i in res:
    print(i)
