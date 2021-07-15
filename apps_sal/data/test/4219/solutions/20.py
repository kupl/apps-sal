N = int(input())
A = [0] * N
x = [0] * N
y = [0] * N
tlist = [0] * N # 1:正直 2:不親切
honest = 0

for i in range(N):
    A[i] = int(input())
    x[i] = []
    y[i] = []
    for j in range(A[i]):
        xt, yt = list(map(int, input().split()))
        x[i].append(xt)
        y[i].append(yt)

for t in range(2**N):
    ns = "0" + str(N) +"b"
    bi = format(t,ns)
    for i in range(N):
        tlist[i] = int(bi[-1-i])
        tflag = True
    for i in range(N):
        for j in range(A[i]):
            if tlist[i] == 1:
                if tlist[x[i][j]-1] != y[i][j]:
                    tflag = False
                    break
        if not tflag:
            break
    if tflag:
        honest = max(honest,sum(tlist))

print(honest)
