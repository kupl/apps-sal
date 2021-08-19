(N, K, Q) = map(int, input().split())
A = list(map(int, input().split()))


def find_maximum(y):
    C = [[]]
    for a in A:
        if a < y:
            if len(C[-1]) > 0:
                C.append([])
        else:
            C[-1].append(a)
    cand_x = []
    for Ci in C:
        m = len(Ci)
        if m >= K:
            Ci.sort()
            cand_x += Ci[:m - K + 1]
    if len(cand_x) >= Q:
        cand_x.sort()
        return (cand_x[Q - 1], cand_x[0])
    else:
        return (10 ** 18, 0)


ans = 10 ** 18
for a in A:
    (x, y) = find_maximum(a)
    ans = min(ans, x - y)
print(ans)
