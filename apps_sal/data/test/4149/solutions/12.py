
from collections import Counter

lim = 2750131 + 10  # 2 * 10**6 + 2


def erato():
    arr = [None] * lim
    arr[1] = 1
    primes = [1]
    for i in range(2, lim):
        if not arr[i]:
            primes.append(i)
            arr[i] = 1
            for j in range(i * 2, lim, i):
                if not arr[j]:
                    arr[j] = j // i

    s = set(primes)
    for i in range(1, len(primes)):
        if i in s:
            arr[i] = primes[i]
    return arr


def __starting_point():
    n = int(input())
    bb = list(map(int, input().split()))
    bb.sort(reverse=True)
    cnt = Counter(bb)
    e = erato()
    res = []
    for b in bb:
        if cnt[e[b]] > 0 and cnt[b] > 0:
            res.append(str(b))
            cnt.subtract({b: 1, e[b]: 1})

    # res = list(map(lambda x: str(e[x]), bb))
    print(" ".join(res))


__starting_point()
