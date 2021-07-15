def main2():
    N, K = map(int, input().split())
    limit = 10**5

    ins = [0 for _ in range(limit + 1)]

    for _ in range(N):
        a, b = map(int, input().split())
        ins[a] += b

    c = 0
    for i in range(1, limit + 1):
        c += ins[i]

        if c >= K:
            print(i)
            return

def __starting_point():
    main2()
__starting_point()
