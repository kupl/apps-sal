import sys
N, L = list(map(int, input().split()))
tastes = [L + x for x in range(N)]

if 0 in tastes:
    print((sum(tastes)))
    return


if L < 0:
    absmin = max(tastes)
    print((sum(tastes) - absmin))
elif L > 0:
    absmin = min(tastes)
    print((sum(tastes) - absmin))
