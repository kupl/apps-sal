import sys


def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        t, d = map(int, input().split())
        S.append((d, t))
    S.sort(reverse=True)
    upperKCount = 0
    appeared = set()
    maxPoint = 0
    for i in range(K):
        maxPoint += S[i][0]
        if S[i][1] not in appeared:
            upperKCount += 1
            appeared |= {S[i][1]}
    maxPoint += upperKCount ** 2
    appeared = set()

    typeMax = []
    typeNum = 0
    typeLower = []
    others = 0
    for d, t in S:
        if t in appeared:
            typeLower.append(d)
            others += 1
        else:
            typeMax.append(d)
            typeNum += 1
            appeared |= {t}
    typeMaxSum = [0] * (typeNum + 1)
    typeLowerSum = [0] * (others + 1)
    for i in range(typeNum):
        typeMaxSum[i + 1] = typeMaxSum[i] + typeMax[i]
    for i in range(others):
        typeLowerSum[i + 1] = typeLowerSum[i] + typeLower[i]
    for k in range(upperKCount + 1, min(typeNum, K) + 1):
        maxPoint = max(maxPoint, k ** 2 + typeMaxSum[k] + typeLowerSum[K - k])
    print(maxPoint)
    return 0


def __starting_point():
    solve()


__starting_point()
