N, M = list(map(int, input().split()))
H = list(map(int, input().split()))

good = [1] * N
for i in range(M):
    A, B = list(map(int, input().split()))
    HA = H[A - 1]
    HB = H[B - 1]
    if HA == HB:
        if good[A - 1]:
            good[A - 1] = 0
        if good[B - 1]:
            good[B - 1] = 0
    elif HA < HB and good[A - 1]:
        good[A - 1] = 0
    elif HB < HA and good[B - 1]:
        good[B - 1] = 0

print((sum(good)))
return

