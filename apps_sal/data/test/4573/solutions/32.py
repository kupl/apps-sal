N = int(input())
Xls = list(map(int, input().split()))
X2ls = sorted(Xls)
M1 = X2ls[N // 2 - 1]
M2 = X2ls[N // 2]
lsans = []
for i in range(N):
    if Xls[i] <= M1:
        M = M2
    else:
        M = M1
    lsans.append(M)
for i in lsans:
    print(i)
