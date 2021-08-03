def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    m = min(a)
    for i in range(n):
        if a[i] % m == 0:
            b.append(a[i])
    b.sort()
    cur = 0
    for j in b:
        while a[cur] % m != 0:
            cur += 1
        a[cur] = j
        cur += 1
    for i in range(1, n):
        if a[i - 1] > a[i]:
            print('NO')
            return
    print('YES')


t = int(input())
for _ in range(t):
    solve()
