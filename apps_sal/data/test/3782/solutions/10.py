N, K, Q = list(map(int, input().split()))
A = list(map(int, input().split()))


def sol(y):
    B = [[]]
    for a in A:
        if a < y and len(B[-1]) > 0:
            B.append([])
        if a >= y:
            B[-1].append(a)

    C = []
    for grp in B:
        grp.sort()
        C += grp[:max(0, len(grp) - K + 1)]
    C.sort()

    return C[Q - 1] - y if len(C) >= Q and C[0] == y else 10**18


ans = 10**18
for y in A:
    ans = min(ans, sol(y))

print(ans)
