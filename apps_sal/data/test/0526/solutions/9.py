import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(n)]

for b in range(10):
    RB = [0] * n
    for j in range(n):
        SCORE = []
        for k in range(m):
            if A[j][k] & (1 << b) == 0:
                SCORE.append(0)
            else:
                SCORE.append(1)

        SCORE = sorted(set(SCORE))

        if len(SCORE) == 2:
            print("TAK")
            ANS = [1] * n
            XOR = 0
            for k in range(n):
                if j == k:
                    continue
                XOR ^= (A[k][0] & (1 << b))

            if XOR == 0:
                for k in range(m):
                    if A[j][k] & (1 << b) != 0:
                        ANS[j] = k + 1
                        print(*ANS)
                        return

            else:
                for k in range(m):
                    if A[j][k] & (1 << b) == 0:
                        ANS[j] = k + 1
                        print(*ANS)
                        return

        elif len(SCORE) == 1:
            RB[j] = SCORE[0]

    XOR = 0
    for i in range(n):
        XOR ^= RB[i]

    if XOR == 0:
        continue
    else:
        print("TAK")
        print(*[1] * n)
        return

else:
    print("NIE")
