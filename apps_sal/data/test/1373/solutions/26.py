#amari = (10**100)%(10**9+7)
def sm(i):
    tmpp = 0
    for j in range(i):
        tmpp += j
    return tmpp, j


def bi(i, N):
    tmpp = 0
    for j in range(i):
        tmpp += N - j

    return tmpp, N - j


def main():
    N, K = list(map(int, input().split()))
    ans = 0
    #loopnum = (N+1) - K + 1
    for i in range(K, N + 2, 1):
        if i == K:
            small, numsmall = sm(i)
            big, numbig = bi(i, N)
            # print(numsmall,numbig)
        else:
            small += numsmall + 1
            numsmall += 1
            big += numbig - 1
            numbig -= 1
        ans += big - small + 1

    return (ans % (10**9 + 7))


print((main()))
