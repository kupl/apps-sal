from sys import stdin
def rs(): return stdin.readline().strip()
def ri(): return int(rs())
def ril(): return list(map(int, rs().split()))


def main():
    N = ri()
    d = {s: i for i, s in enumerate('MARCH')}
    l = [0] * 5
    for i in range(N):
        s = rs()[0]
        if s in d:
            l[d[s]] += 1
    ans = 0
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                ans += l[i] * l[j] * l[k]
    print(ans)


def __starting_point():
    main()


__starting_point()
