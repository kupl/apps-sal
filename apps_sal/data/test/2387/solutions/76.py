def main():
    n = int(input())
    Ss = [input() for _ in range(n)]
    U = [[0, 0] for _ in range(n)]
    for i in range(n):
        for c in Ss[i]:
            if c == "(":
                U[i][1] += 1
            else:
                if U[i][1] == 0:
                    U[i][0] += 1
                else:
                    U[i][1] -= 1
    L, R = 0, 0
    P = []
    for i in range(n):
        if U[i][0] == 0 and U[i][1] > 0:
            L += U[i][1]
        elif U[i][0] > 0 and U[i][1] == 0:
            R += U[i][0]
        elif U[i][0] > 0 and U[i][1] > 0:
            P.append([U[i][0], U[i][1]])
    P.sort(key=lambda x: (x[0] - x[1], x[0], -x[1]))
    if L == 0 and R == 0 and len(P) == 0:
        print("Yes")
    elif (L == 0 or R == 0) and len(P) > 0:
        print("No")
    else:
        f = True
        for i in range(len(P)):
            L -= P[i][0]
            if L < 0:
                f = False
                break
            L += P[i][1]
        if L == R and f:
            print("Yes")
        else:
            print("No")


def __starting_point():
    main()


__starting_point()
