
def II(): return int(input())
def MII(): return list(map(int, input().split()))
def LII(): return list(map(int, input().split()))


def main():
    N, M = MII()
    s = []
    for _ in range(M):
        s.append(list(map(int, input().split()))[1:])
    p = LII()

    ans = 0
    for i in range(2**N, 2**(N + 1)):
        b = bin(i)[3:]
        t = [0] * M
        for j, sj in enumerate(s):
            for k, bi in enumerate(list(b)):
                if bi == '1' and k + 1 in sj:
                    t[j] += 1
            if t[j] % 2 != p[j]:
                ans -= 1
                break
        ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()
