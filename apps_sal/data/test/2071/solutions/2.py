def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    roundup = []
    rounddown = []
    sumsofar = []

    for i, (a, b) in enumerate(zip(reversed(A), reversed(B))):
        ssf = sumsofar[-1] if sumsofar else 0
        t = roundup[-1] if roundup else 0
        roundup.append(t + ssf + b * (1 + 2 * i))
        t = rounddown[-1] if rounddown else 0
        rounddown.append(t + ssf + a * (1 + 2 * i))
        sumsofar.append(ssf + a + b)

    roundup = list(reversed(roundup))
    rounddown = list(reversed(rounddown))
    sumsofar = list(reversed(sumsofar))
    bestres = 0
    sofar = 0

    # for u, d in zip(roundup, rounddown):
    # 	print(u, d, '-')

    for i, (a, b) in enumerate(zip(A, B)):
        rup, rdo = roundup, rounddown
        if i % 2:
            a, b = b, a
            rup, rdo = rdo, rup
        # print(i, sofar + rup[i])
        bestres = max(bestres, sofar + rup[i] + sumsofar[i] * 2 * i)
        sofar += a * 2 * i
        sofar += b * (2 * i + 1)
        bestres = max(bestres, sofar)

    print(bestres)


def __starting_point():
    main()


__starting_point()
