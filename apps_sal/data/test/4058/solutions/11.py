(n, r) = [int(x) for x in input().split()]
ns = [int(x) for x in input().split()]


def fin(i):
    p = need + r - 1
    last = max(need - r, -1)
    j = min(len(ns) - 1, p)
    while j > last:
        if ns[j] > 0:
            return j + r
        j -= 1
    return -1


need = 0
ans = 0
while need < len(ns):
    ans += 1
    need = fin(need)
    if need == -1:
        print(-1)
        quit()
print(ans)
