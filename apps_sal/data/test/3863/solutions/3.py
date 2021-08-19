import sys
read = sys.stdin.read
readline = sys.stdin.readline
(n, k) = list(map(int, readline().split()))
MOD = 10 ** 9 + 7


def divisor_list(N):
    if N == 1:
        return [1]
    res = []
    for i in range(1, N):
        if i * i >= N:
            break
        if N % i == 0:
            res.append(i)
            res.append(N // i)
    if i * i == N:
        res.append(i)
    return sorted(res)


if n & 1:
    p = [i for i in divisor_list(n)]
    r = {pi: pow(k, (pi + 1) // 2, MOD) for pi in p}
    for pi in p:
        for pj in p:
            if pj >= pi:
                break
            if pi % pj == 0:
                r[pi] -= r[pj]
    ans = 0
    for (pi, v) in list(r.items()):
        ans += v * pi
    ans %= MOD
    print(ans)
else:
    p = [1] + [i for i in divisor_list(n) if i % 2 == 0 and i != 2]
    r = {pi: pow(k, (pi + 1) // 2, MOD) for pi in p}
    for pi in p:
        for pj in p:
            if pj >= pi:
                break
            if pi % pj == 0:
                r[pi] -= r[pj]
    ans = 0
    for (pi, v) in list(r.items()):
        if pi == 1:
            ans += v
        else:
            ans += v * (pi // 2)
    ans %= MOD
    print(ans)
