

def solve(T, V, velocity):
    accT = 1
    for t, max_v in zip(T, V):
        for i in range(accT, accT + 2 * t):
            velocity[i] = min(velocity[i], velocity[i - 1] + 0.5, max_v)
        accT += 2 * t


def main():

    N, *A = list(map(int, open(0).read().split()))
    T = A[:N]
    V = A[N:]

    INF = 10**10

    velocity = [INF] * (sum(T) * 2 + 1)
    velocity[0] = 0
    velocity[-1] = 0
    solve(T, V, velocity)
    velocity = velocity[::-1]
    solve(T[::-1], V[::-1], velocity)

    ans = 0
    pre_v = velocity[0]
    for v in velocity[1:]:
        ans += (pre_v + v) * 0.25
        pre_v = v

    print(ans)


def __starting_point():
    main()


__starting_point()
