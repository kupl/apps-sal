def main():
    N = int(input())
    S = list(map(int, input().split()))
    INF = float('inf')
    n = 2 ** N + 1
    S.sort()
    parents = [S[-1]]
    S[-1] = INF
    for _ in range(N):
        checking = 2
        parents.sort()
        tmp = parents[::-1]
        for i in tmp:
            while True:
                if S[-checking] < i:
                    parents.append(S[-checking])
                    S[-checking] = INF
                    break
                else:
                    checking += 1
                if checking == n:
                    print('No')
                    return
    else:
        print('Yes')


def __starting_point():
    main()


__starting_point()
