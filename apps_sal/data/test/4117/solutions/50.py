def main():
    N = int(input())
    L = list(map(int, input().split()))
    if N < 3:
        print(0)
        return
    ans = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                Li = L[i]
                Lj = L[j]
                Lk = L[k]
                if Li != Lj and Lj != Lk and (Lk != Li) and (Li < Lj + Lk) and (Lj < Li + Lk) and (Lk < Li + Lj):
                    ans += 1
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
