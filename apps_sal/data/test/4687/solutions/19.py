

def main():
    N, K = list(map(int, input().split()))
    box = []
    for _ in range(N):
        ab = list(map(int, input().split()))
        box.append(ab)

    box.sort(key= lambda x: x[0])
    ans = 0
    for b in box:
        if ans + b[1] < K:
            ans += b[1]
        else:
            print((b[0]))
            return


def __starting_point():
    main()

__starting_point()
