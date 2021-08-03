def main():
    N, K = list(map(int, input().split()))
    l = []
    cnt = 0
    for _ in range(N):
        a, b = list(map(int, input().split()))
        l.append((a, b))
    l.sort(key=lambda x: x[0])
    for a, x in l:
        cnt += x
        if cnt >= K:
            print(a)
            return


def __starting_point():
    main()


__starting_point()
