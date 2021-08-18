
from collections import Counter


def resolve():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    CNT = Counter(A)

    for i in range(M):
        b, c = list(map(int, input().split()))
        CNT[c] += b

    cards = sorted(list(CNT.items()), key=lambda x: x[0], reverse=True)

    ans = 0
    for key, cnt in cards:
        if N > cnt:
            ans += key * cnt
            N -= cnt
        else:
            ans += key * N
            print(ans)
            return


def __starting_point():
    resolve()


__starting_point()
