(N, M) = map(int, input().split())
res = 0
flag = True
INF = 100000000000
stepList = [INF] * (N + 1)
stepList[0] = 1
stepList[1] = 1


def stepF(K):
    if K == 0:
        return stepList[0]
    else:
        for i in range(1, K + 1):
            if i == 1:
                pass
            elif stepList[i] == INF:
                stepList[i] = stepList[i - 2] + stepList[i - 1]
        return stepList[K]


if M == 0:
    res = stepF(N)
else:
    List = []
    for i in range(M):
        List.append(int(input()))
    for i in range(M):
        if i == 0:
            res = stepF(List[i] - 1)
        else:
            if List[i] - List[i - 1] == 1:
                flag = False
                break
            res = res * stepF(List[i] - List[i - 1] - 2)
    res = res * stepF(N - List[M - 1] - 1)
if flag:
    print(res % 1000000007)
else:
    print(0)
