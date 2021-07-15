def __starting_point():
    N = int(input())
    ans = 0
    for n in range(1, N+1):
        if len(str(n))%2 != 0:
            ans += 1

    print(ans)
__starting_point()
