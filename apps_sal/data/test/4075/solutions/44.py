N = None
M = None
S = []
P = []


def __starting_point():
    N, M = map(int, input().split())
    for _ in range(M):
        row = list(map(int, input().split()))[1:]
        S.append(row)
    P = list(map(int, input().split()))
    ans = 0
    for bit in range(1 << N):
        on_switches = []
        light = 0
        for i in range(N):
            if bit >> i & 1:
                on_switches.append(i)
        for i in range(M):
            cnt = 0
            for s in S[i]:
                for on_switch in on_switches:
                    if s == on_switch + 1:
                        cnt += 1
            if cnt % 2 == P[i]:
                light += 1
        if light == M:
            ans += 1
    print(ans)


__starting_point()
