X, K, D = list(map(int, input().split()))
if abs(X) > D * K:
    abso = abs(X) - D * K
    print(abso)
    return
div = abs(X) // D
mod = abs(X) % D  # +側の最小値
if (K - div) % 2 == 0:  # K-div:+側での絶対値の最小値までたどり着く回数
    print(mod)
else:
    print((D - mod))
