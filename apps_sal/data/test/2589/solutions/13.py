def solve():
    (n, x) = map(int, input().split())
    a = list(map(int, input().split()))
    if all(map(lambda i: a[i] % x == 0, range(n))):
        print(-1)
        return
    s = sum(a)
    (l, r) = (n + 1, n + 1)
    for i in range(n):
        if a[i] % x != 0:
            l = min(i, l)
            r = i
    if s % x != 0:
        print(n)
        return
    print(max(n - l - 1, r))


t = int(input())
for _ in range(t):
    solve()
