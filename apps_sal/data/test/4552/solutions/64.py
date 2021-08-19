from itertools import product
N = int(input())
lsF = [[]]
for i in range(N):
    lsF.append(list(map(int, input().split())))
lsP = [[]]
for i in range(N):
    lsP.append(list(map(int, input().split())))
bita = list(product(range(2), repeat=10))
bita.pop(0)
ans = -10 ** 10
for bit in bita:
    count = [0 for i in range(N + 1)]
    for i in range(10):
        for j in range(1, N + 1):
            count[j] += bit[i] * lsF[j][i]
    benifit = 0
    for i in range(1, N + 1):
        benifit += lsP[i][count[i]]
    ans = max(ans, benifit)
print(ans)
