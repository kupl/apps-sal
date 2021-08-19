from collections import Counter
n = int(input())


def kC2(k):
    return k * (k - 1) // 2


A = list(map(int, input().split()))
AC = Counter(A)
total = sum((kC2(v) for v in AC.values()))
print(*[total - kC2(AC[a]) + kC2(AC[a] - 1) for a in A], sep='\n')
