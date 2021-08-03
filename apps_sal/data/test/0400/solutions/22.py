import math as m


def solve():
    n, k = (int(i) for i in input().split())

    ai = [int(i) for i in input().split()]

    cnt = 0

    if(k > 100 * len(ai) - sum(ai)):
        k = 100 * len(ai) - sum(ai)

    for i in range(len(ai)):
        cnt += m.floor(ai[i] / 10)
        ai[i] = ai[i] % 10

    ai.sort(reverse=True)

    for i in range(len(ai)):
        diff = 10 - ai[i]
        if diff <= k:
            k -= diff
            cnt += 1

    cnt += m.floor(k / 10)

    return cnt


print(solve())
