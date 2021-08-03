from itertools import groupby


def mp3(n, I, a):
    k = int((I * 8) / n)
    d = 1 << k
    c = [len(list(group)) for (key, group) in groupby(sorted(a))]
    chgs = sum(c[d:])
    ans = chgs
    for i in range(0, len(c) - d):
        chgs += c[i]
        chgs -= c[i + d]
        ans = min(ans, chgs)
    return ans


def __starting_point():
    nn, II = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    print(mp3(nn, II, aa))


__starting_point()
