def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n % 2 == 1:
        if a[n // 2] != b[n // 2]:
            print('No')
            return
    u, v = list(), list()

    def add(s, p, q):
        if p > q:
            p, q = q, p
        s.append((p, q))
    for i in range(n // 2):
        add(u, a[i], a[n - i - 1])
        add(v, b[i], b[n - i - 1])
    if sorted(u) == sorted(v):
        print('Yes')
    else:
        print('No')


t = int(input())
for _ in range(t):
    solve()
