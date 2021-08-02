from itertools import permutations


def f(a):
    ans = 0
    for i in range(n):
        cur = a[i]
        for j in range(i, n):
            cur = min(cur, a[j])
            ans += cur
    return ans


n, m = list(map(int, input().split()))
ans = max(list(map(f, permutations(list(range(1, n + 1))))))
for a in permutations(list(range(1, n + 1))):
    m -= f(a) == ans
    if not m:
        print(*a)
        break
