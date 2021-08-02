N, M, X = list(map(int, input().split()))

li = []
ans = 100000000000000000000000000000000

for j in range(N):
    a = list(map(int, input().split()))
    li.append(a)

for k in range(2**N):
    temp = 0
    skill = [0] * M
    k = str(bin(k))
    k = k[2:]
    while len(k) != N:
        k = "0" + k
    for l in range(N):
        if k[l] == "1":
            temp += li[l][0]
            for m in range(1, M + 1):
                skill[m - 1] += li[l][m]
    if min(skill) >= X:
        if ans > temp:
            ans = temp
if ans == 100000000000000000000000000000000:
    print((-1))
else:
    print(ans)
