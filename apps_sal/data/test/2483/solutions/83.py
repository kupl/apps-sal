from operator import itemgetter


def resolve():
    (N, C) = list(map(int, input().split()))
    STC = sorted([list(map(int, input().split())) for _ in range(N)], key=itemgetter(2, 0))
    counts = [0] * (10 ** 5 + 1)
    (prevt, prevc) = (-1, -1)
    for stc in STC:
        (s, t, c) = stc
        if prevt == s and prevc == c:
            counts[s] += 1
        else:
            counts[s - 1] += 1
        counts[t] -= 1
        (prevt, prevc) = (t, c)
    for i in range(1, 10 ** 5 + 1):
        counts[i] += counts[i - 1]
    print(max(counts))


if '__main__' == __name__:
    resolve()
