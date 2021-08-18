'''input
3 2
1 3 0
'''


def solve():
    n, k = list(map(int, input().split()))
    flipVal = (1 << k) - 1
    l = list(map(int, input().split()))
    D = {}
    D[0] = 1
    for i in range(1, n):
        l[i] ^= l[i - 1]
    for i in range(0, n):
        l[i] = min(l[i], l[i] ^ flipVal)
        if l[i] in D:
            D[l[i]] += 1
        else:
            D[l[i]] = 1
    total = n * (n + 1) // 2
    bad = 0
    for i in D:
        temp = D[i]
        tot = temp // 2
        bad += tot * (tot - 1) // 2
        tot = temp - tot
        bad += tot * (tot - 1) // 2
    print(total - bad)
    return


t = 1
while t > 0:
    t -= 1
    solve()
