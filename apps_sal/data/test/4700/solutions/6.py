N, M = list(map(int, input().split()))
H = list(map(int, input().split()))

good = [1] * N
for i in range(M):
    A, B = list(map(int, input().split()))
    A, B = A - 1, B - 1
    HA = H[A]
    HB = H[B]
    if HA == HB:
        if good[A]:
            good[A] = 0
        if good[B]:
            good[B] = 0
    elif HA < HB and good[A]:
        good[A] = 0
    elif HB < HA and good[B]:
        good[B] = 0

print((sum(good)))
return
