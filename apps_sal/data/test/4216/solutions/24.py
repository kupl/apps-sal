def __starting_point():
    N = int(input())
    i = 1
    ans = 10
    while i * i <= N:
        if N % i == 0:
            f = max(len(str(i)), len(str(N // i)))
            ans = min(f, ans)
        i += 1

    print(ans)


__starting_point()
