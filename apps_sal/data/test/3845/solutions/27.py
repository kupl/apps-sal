import sys
input = sys.stdin.readline


def main():
    A, B = [int(x) for x in input().split()]

    common = min(A, B)

    ans = [["-"] * 100 for j in range(100)]

    if A == B == 1:
        print(1, 2)
        print(".
        return

    reverse=False
    if B == 1:
        reverse=True
        A, B=B, A

    A -= 1
    B -= 1
    Borg=B
    Aorg=A

    Arow=-(-A // 50) * 2
    Brow=-(-B // 50) * 2

    for i in range(Brow):
        if i % 2 == 0:
            for j in range(100):
                if j % 2 == 0:
                    if Borg <= 0:
                        ans[i][j]="."
                    else:
                        ans[i][j]= "
                        Borg -= 1
                else:
                    ans[i][j]="."
        else:
            for j in range(100):
                ans[i][j]="."

    for i in range(Brow, Brow + Arow):
        if (i - Brow) % 2 == 0:
            for j in range(100):
                ans[i][j]= "
        else:
            for j in range(100):
                if j % 2 == 0:
                    if Aorg <= 0:
                        ans[i][j]= "
                    else:
                        ans[i][j]="."
                        Aorg -= 1
                else:
                    ans[i][j]= "

    for i in range(Brow + Arow, 100):
        for j in range(100):
            ans[i][j]= "

    print(100, 100)
    if reverse:
        for i in range(100):
            for j in range(100):
                if ans[i][j] == "
                    print(".", end="")
                else:
                    print("
            print()
    else:
        for a in ans:
            print("".join(a))


def __starting_point():
    main()


__starting_point()
