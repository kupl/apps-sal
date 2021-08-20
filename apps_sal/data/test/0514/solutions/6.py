t = int(input())
for _ in range(t):
    (n, d) = map(int, input().split())
    (u, v) = (max(0, int(d ** 0.5 - 1000)), min(n, int(d ** 0.5 + 1000)))
    for i in range(u, v + 1):
        if i + d // (i + 1) + int(bool(d % (i + 1))) <= n:
            print('YES')
            break
    else:
        print('NO')
