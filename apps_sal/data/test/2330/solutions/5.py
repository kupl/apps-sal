for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    a = [*list(map(int, input().split()))]
    if m < n or (n == 2 and m == 2):
        print(-1)
    else:
        cost = x = y = 0
        mn = float('inf')
        for i in range(n):
            t = a[i] + a[i - 1]
            cost += t
            if t < mn:
                mn = min(mn, t)
                (x, y) = (i + 1, n if i == 0 else i)
        print(cost + (m - n) * mn)
        for i in range(n - 1):
            print(i + 1, (i + 2) % (n + 1))
        print(n, 1)
        for i in range(m - n):
            print(x, y)
