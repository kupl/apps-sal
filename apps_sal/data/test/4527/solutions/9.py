import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s); sys.stdout.write('\n')
def wi(n): sys.stdout.write(str(n)); sys.stdout.write('\n')
def wia(a, sep=' '): sys.stdout.write(sep.join([str(x) for x in a])); sys.stdout.write('\n')


def solve(n, segs):
    vals = set()
    for l, r in segs:
        vals.add(l)
        vals.add(r)
    vals = sorted(list(vals))
    d = {x: i for i, x in enumerate(vals)}
    m = len(vals)

    c_segs = []
    r_segs = [[] for _ in range(m)]
    for l, r in segs:
        ll = d[l]
        rr = d[r]
        c_segs.append((ll, rr))
        r_segs[ll].append(rr)

    dp = [[0] * m for _ in range(m)]
    for ln in range(1, m + 1):
        for l in range(m):
            r = l + ln - 1
            if r >= m:
                continue
            if l + 1 <= r:
                dp[l][r] = dp[l + 1][r]
            for rr in r_segs[l]:
                if rr >= r:
                    continue
                dp[l][r] = max(dp[l][r], dp[l][rr] + dp[rr + 1][r])
            if r in r_segs[l]:
                dp[l][r] += 1

    return dp[0][-1]


def main():
    for _ in range(ri()):
        n = ri()
        segs = []
        for i in range(n):
            l, r = ria()
            segs.append((l, r))
        wi(solve(n, segs))


def __starting_point():
    main()


__starting_point()
