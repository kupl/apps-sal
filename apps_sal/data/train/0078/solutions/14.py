def gns():
    return list(map(int, input().split()))


t = int(input())


def one():
    (n, m) = gns()
    mp = []
    ns = [0] * n
    ms = [0] * m
    for i in range(n):
        mp.append(input())
        for j in range(m):
            if mp[-1][j] == '*':
                ns[i] += 1
                ms[j] += 1
    min_n = max(ns)
    min_m = max(ms)
    min_ns = set([i for i in range(n) if ns[i] == min_n])
    min_ms = set([i for i in range(m) if ms[i] == min_m])
    ans = n - min_n + m - min_m
    for i in min_ns:
        for j in min_ms:
            if mp[i][j] == '.':
                print(ans - 1)
                return
    print(ans)


for i in range(t):
    one()
