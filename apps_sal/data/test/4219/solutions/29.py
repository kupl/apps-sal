N = int(input())
XY = [[[]] for n in range(N + 1)]
for n in range(1, N + 1):
    a = int(input())
    XY[n] = [list(map(int, input().split())) for _ in range(a)]

maxH = 0
for mask_i in range(1 << N):

    H = [0] * (N + 1)
    for n in range(N):
        if mask_i >> n & 1:
            H[n + 1] = 1

    ok = True
    for n in range(1, N + 1):
        if H[n] == 1:
            for x, y in XY[n]:
                if H[x] != y:
                    ok = False
                    break
    if ok:
        maxH = max(maxH, sum(H))

print(maxH)
