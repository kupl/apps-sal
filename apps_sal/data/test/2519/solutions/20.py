

def main():
    N, K = list(map(int, input().split()))
    tmp, ans = 0.0, 0.0
    P = list(map(int, input().split()))

    for i in range(N):
        if i < K:
            tmp += P[i]
            ans = tmp
        else:
            tmp += P[i] - P[i - K]
            ans = max(ans, tmp)

    ans = (ans + K) / 2

    print(ans)


def __starting_point():
    main()


__starting_point()
