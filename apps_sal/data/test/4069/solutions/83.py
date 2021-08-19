(X, K, D) = list(map(int, input().split()))


def sign(x):
    return 1 if x >= 0 else -1


ans = abs(X) - K * D
if abs(X) - K * D < 0:
    divs = abs(X) // D
    mods = abs(X) % D
    nums = K - divs
    ans = abs(mods - nums % 2 * D)
print(ans)
