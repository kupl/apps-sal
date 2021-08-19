import sys


def is_feasible(cnt, L, R):
    n = len(R)
    inter = [(L[i], R[i]) for i in range(n)]
    AUX = []
    feasible = True
    for x in range(n):
        for p in inter:
            if p[0] == x:
                AUX.append(p[1])
        while AUX and min(AUX) < x:
            AUX.remove(min(AUX))
        for quantity in range(cnt[x]):
            if AUX:
                AUX.remove(min(AUX))
            else:
                feasible = False
    return feasible


(n, q) = list(map(int, sys.stdin.readline().split()))
L = [0 for i in range(n)]
R = [n - 1 for i in range(n)]
for restriction in range(q):
    (t, l, r, v) = list(map(int, sys.stdin.readline().split()))
    if t == 1:
        for k in range(l - 1, r):
            L[k] = max(L[k], v - 1)
    else:
        for k in range(l - 1, r):
            R[k] = min(R[k], v - 1)
is_possible = all(map(lambda x, y: x <= y, L, R))
if not is_possible:
    print(-1)
else:
    cnt = {x: L.count(x) for x in range(n)}
    had_pair = True
    while had_pair:
        had_pair = False
        for x in range(n - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                if cnt[x] > cnt[y] + 1:
                    cnt[x] -= 1
                    cnt[y] += 1
                    has_pair = True
                    if not is_feasible(cnt, L, R):
                        cnt[x] += 1
                        cnt[y] -= 1
                        has_pair = False
                    had_pair = had_pair or has_pair
    ans = sum([cnt[x] * cnt[x] for x in range(n)])
    print(ans)
