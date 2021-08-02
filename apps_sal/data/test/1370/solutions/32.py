from operator import add

INF = 10**6

H, W, K = list(map(int, input().split()))
Ass = [list(map(int, input().rstrip())) for _ in range(H)]


def check(chocoss):
    if max(list(map(max, chocoss))) > K:
        return INF

    L = len(chocoss)
    num = 0
    Bs = [0] * L
    for j in range(W):
        for i in range(L):
            if Bs[i] + chocoss[i][j] > K:
                num += 1
                Bs = [chocoss[i][j] for i in range(L)]
                break
        else:
            for i in range(L):
                Bs[i] += chocoss[i][j]

    return num


ans = INF
for ptn in range(1 << (H - 1)):
    chocoss = [Ass[0]]
    num = 0
    for i in range(H - 1):
        if (ptn >> i) & 1:
            chocoss.append(Ass[i + 1])
            num += 1
        else:
            chocoss[-1] = list(map(add, chocoss[-1], Ass[i + 1]))

    num += check(chocoss)
    if num < ans:
        ans = num

print(ans)
