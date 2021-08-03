#!python3

def LI(): return list(map(int, input().split()))


# input
N, P = LI()
S = input()


def solve2():
    ans = 0
    for i in range(N):
        if int(S[i]) % 2 == 0:
            ans += i + 1
    return ans


def solve5():
    ans = 0
    for i in range(N):
        if int(S[i]) % 5 == 0:
            ans += i + 1
    return ans


def solve():
    d = [0] * P
    d[0] = 1
    w = 0
    ans = 0
    m = 1
    for s in S[::-1]:
        x = int(s)
        v = x * m % P
        w = (w + v) % P
        ans += d[w]
        d[w] += 1
        m = 10 * m % P
    return ans


def main():
    if P == 2:
        ans = solve2()
    elif P == 5:
        ans = solve5()
    else:
        ans = solve()
    print(ans)


def __starting_point():
    main()


__starting_point()
