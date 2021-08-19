def main():
    (N, K) = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    no_need = 0
    sub = 0
    for ai in A:
        if sub + ai < K:
            sub += ai
            no_need += 1
        else:
            no_need = 0
    print(no_need)


def __starting_point():
    main()


__starting_point()
