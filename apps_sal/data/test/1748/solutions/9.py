def findMaxTemp(psT, v, start, minus):
    l = start - 1
    r = len(psT)

    while r - l > 1:
        m = l + (r - l) // 2
        val = psT[m] - minus
        if val < v:
            l = m
        else:
            r = m

    return l, r


def solve():
    N = int(input())
    V = list(map(int, input().split()))
    T = list(map(int, input().split()))

    ans = [0 for _ in range(N)]
    partialAns = [0 for _ in range(N)]
    cnt = [0 for _ in range(N)]
    minus = 0
    psT = T[:]

    for i in range(1, N):
        psT[i] += psT[i - 1]

    for i in range(len(V)):
        l, r = findMaxTemp(psT, V[i], i, minus)

        if r == i:
            partialAns[r] += V[i]
        elif r == len(psT):
            cnt[i] += 1
        else:
            cnt[i] += 1
            cnt[l + 1] -= 1
            value = V[i] - (psT[l] - minus)
            partialAns[r] += value

        minus = psT[i]

    for i in range(1, N):
        cnt[i] += cnt[i - 1]

    for i in range(N):
        ans[i] += partialAns[i]
        ans[i] += cnt[i] * T[i]

    return ans


for x in solve():
    print(x, end=' ')
