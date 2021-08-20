def main(X, N, P):
    ans = None
    min_dis = 100000000.0
    for i in range(102):
        if i in P:
            continue
        if abs(X - i) < min_dis:
            ans = i
            min_dis = abs(X - i)
    return ans


def __starting_point():
    (X, N) = list(map(int, input().split()))
    P = list(map(int, input().split()))
    ans = main(X, N, P)
    print(ans)


__starting_point()
