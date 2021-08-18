n, m = list(map(int, input().split()))
l = []
for i in range(1 << n):
    tmp = str(bin(i))[2:]
    l.append(tmp.zfill(n))
K = [list(map(int, input().split())) for _ in range(m)]
P = list(map(int, input().split()))
ans = 0
for i in range(len(l)):
    O = []
    for j in range(m):
        ON = 0
        for ii in range(K[j][0]):
            if l[i][K[j][ii + 1] - 1] == "1":
                ON += 1
        if ON % 2 == P[j]:
            O.append(1)
        else:
            O.append(0)
    if sum(O) == m:
        ans += 1
print(ans)
