def solve():
    import math
    N, M = [int(i) for i in input().split()]
    A = list(map(int, input().split()))

    lcm = A[0]
    for i in range(1, N):
        lcm = lcm * A[i] // math.gcd(lcm, A[i])
    first = lcm // 2

    ans_exists = True
    for i in range(N):
        if first % A[i] == 0:
            ans_exists = False

    if ans_exists:
        ans = int((M - first) // lcm + 1)
        print(ans)
    else:
        print('0')


def __starting_point():
    solve()


__starting_point()
