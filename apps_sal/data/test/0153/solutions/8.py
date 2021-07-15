n, k, M = list(map(int, input().split()))
t = sorted(map(int, input().split()))

def calc(x):
    tot = x * sum(t)
    if tot > M:
        return 0
    tans = x * (k + 1)
    for i in range(k - 1):
        if t[i] * (n - x) + tot <= M:
            tot += t[i] * (n - x)
            tans += n - x
        else:
            tans += (M - tot) // t[i]
            break
    return tans

print(max([calc(x) for x in range(n + 1)]))

