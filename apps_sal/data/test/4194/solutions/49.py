def __starting_point():
    (n, m) = map(int, input().split())
    A = list(map(int, input().split()))
    ans = n - sum(A)
    if ans >= 0:
        print(ans)
    else:
        print(-1)


__starting_point()
