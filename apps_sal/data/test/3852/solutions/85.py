def main():
    N = int(input())
    A = list(map(int, input().split()))
    if all([a > 0 for a in A]):
        print(N - 1)
        for i in range(N - 1):
            print(i + 1, i + 2)
        return
    elif all([a <= 0 for a in A]):
        print(N - 1)
        for i in range(N - 1, 0, -1):
            print(i + 1, i)
        return
    else:
        if abs(max(A)) >= abs(min(A)):
            print(2 * N - 1)
            for i in range(N):
                print(A.index(max(A)) + 1, i + 1)
            for i in range(N - 1):
                print(i + 1, i + 2)
            return
        else:
            print(2 * N - 1)
            for i in range(N):
                print(A.index(min(A)) + 1, i + 1)
            for i in range(N - 1, 0, -1):
                print(i + 1, i)
            return


def __starting_point():
    main()


__starting_point()
