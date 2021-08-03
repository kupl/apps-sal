def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    mp = dict()
    ans = 0
    for i in range(N):
        x = i - A[i]
        ans += mp.get(x, 0)
        y = A[i] + i
        mp[y] = mp.get(y, 0) + 1
    print(ans)


def __starting_point():
    resolve()


__starting_point()
