from itertools import product

INF = 10 ** 9

N, *A = list(map(int, input().split()))
L = [int(input()) for _ in range(N)]


def estimate(lst):
    if any(not p for p in lst):
        return INF

    ret = 0
    for p, g in zip(lst, A):
        ret += abs(g - sum(p)) + (len(p) - 1) * 10
    return ret


ans = INF
for prd in product(list(range(4)), repeat=N):
    pieces = [[] for _ in range(3)]
    for bamboo_ind, target_kadomatsu in enumerate(prd):
        if target_kadomatsu == 3:
            continue
        pieces[target_kadomatsu].append(L[bamboo_ind])
    if ans > (res := estimate(pieces)):
        ans = res
print(ans)
