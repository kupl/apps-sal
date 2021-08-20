from collections import Counter
(n, m) = list(map(int, input().split()))
ns = list(map(int, input().split()))
ms = list(map(int, input().split()))
target = Counter({i: m for (i, m) in enumerate(ms, 1) if m != 0})


def check():
    for i in range(n - summs + 1):
        if target == Counter(ns[i:i + summs]):
            return True
    return False


summs = sum(ms)
print(['NO', 'YES'][check()])
