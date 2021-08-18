def abc128_c():
    N, M = list(map(int, input().split()))

    connected_switches = []
    for i in range(M):
        tmp = list(map(int, input().split()))[1:]
        connected_switches.append(tmp)

    p = list(map(int, input().split()))

    ans = 0

    for i in range(2 ** N):
        for j in range(M):
            on_switch_count = 0
            for k in range(N):
                if k + 1 in connected_switches[j] and ((i >> k) & 1):
                    on_switch_count += 1

            if on_switch_count % 2 != p[j]:
                break

            if j == (M - 1):
                ans += 1

    print(ans)


def __starting_point():
    abc128_c()


__starting_point()
