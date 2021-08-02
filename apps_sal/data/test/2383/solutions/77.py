def main():
    N = int(input())
    A = list(map(int, input().split()))
    breakcount = 0
    cnt = 1
    for i in range(N):
        if A[i] != cnt:
            breakcount += 1
        else:
            cnt += 1
    if cnt == 1:
        print((-1))
        return
    print(breakcount)


def __starting_point():
    main()


__starting_point()
