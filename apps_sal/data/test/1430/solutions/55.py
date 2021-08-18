
from itertools import accumulate


def resolve():
    N, K = map(int, input().split())
    S = input()

    L = []
    pre = "1"
    cnt = 0
    for i in range(N):
        if pre == S[i]:
            cnt += 1
        else:
            L.append(cnt)
            cnt = 1
        pre = S[i]
    L.append(cnt)
    if pre == "0":
        L.append(0)

    length = 2 * K + 1

    if len(L) <= length:
        return print(N)

    acc = [0] + list(accumulate(L))
    ans = 0
    for i in range(0, len(L), 2):
        left = i
        right = min(i + length, len(L))
        tmp = acc[right] - acc[left]

        ans = max(ans, tmp)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
