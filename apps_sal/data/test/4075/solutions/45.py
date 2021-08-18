import sys
input = sys.stdin.readline


def slove():
    N, M = map(int, input().split())
    light = []
    for i in range(M):
        connecting_sw = list(map(int, input().split()))
        light.append(connecting_sw[1:])
    on = list(map(int, input().split()))

    ans = 0
    for i in range(1 << N):
        light_on = [0] * M
        for j in range(N):
            if i >> j & 1:
                a = 0
                for item in light:
                    if j + 1 in item:
                        light_on[a] = (light_on[a] + 1) % 2
                    a += 1
        a = 0
        for i in range(M):
            if on[i] == light_on[i]:
                a += 1
                continue
            break
        if a == M:
            ans += 1

    print(ans)


def __starting_point():
    slove()


__starting_point()
