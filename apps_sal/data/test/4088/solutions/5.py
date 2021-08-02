from collections import Counter

T = int(input())

for t in range(T):
    S = input()
    M = int(input())
    B = [int(_) for _ in input().split()]

    Y = ['' for _ in range(M)]
    expected_scores = [0] * M
    cc = Counter(S)
    for _c in range(ord('z'), ord('a') - 1, -1):
        c = chr(_c)
        if not cc[c]:
            continue
        # print('before', c, Y, expected_scores)
        poss = []
        next_expected_scores = list(expected_scores)
        for pos in range(M):
            if Y[pos] != '':
                continue
            if B[pos] == expected_scores[pos]:
                poss.append(pos)
                for p in range(M):
                    next_expected_scores[p] += abs(p - pos)

        if len(poss) <= cc[c]:
            expected_scores = next_expected_scores
            for p in poss:
                Y[p] = c
        # print('after', c, Y, expected_scores)

    print(''.join(Y))
