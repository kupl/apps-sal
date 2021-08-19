def solve():
    (n, m, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    for i in range(n - 1):
        if a[i] >= a[i + 1] - k:
            m += min(a[i], a[i] - max(a[i + 1] - k, 0))
            continue
        elif a[i] + m < a[i + 1] - k:
            print('NO')
            return
        else:
            m -= max(0, a[i + 1] - k - a[i])
    print('YES')


t = int(input())
for _ in range(t):
    solve()
