import numpy as np

N, K = list(map(int, input().split()))
As_lis = list(map(int, input().split()))

As_arr = np.array(As_lis)
S = np.sum(As_arr)

smaller_factors = []
larger_factors = []
for i in range(1, int(S ** 0.5) + 1):
    if S % i == 0:
        smaller_factors.append(i)
        larger_factors.append(S // i)

for fac in larger_factors:
    mods = As_arr % fac
    k = np.sum(np.sort(mods)[:N - np.sum(mods) // fac])
    if k <= K:
        print(fac)
        return

for fac in reversed(smaller_factors):
    mods = As_arr % fac
    k = np.sum(np.sort(mods)[:N - np.sum(mods) // fac])
    if k <= K:
        print(fac)
        return


