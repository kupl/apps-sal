t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    cost = 0
    a = []
    for i in range(n):
        c = list(map(int, input().split()))
        a.append(c)
    r = (n + m - 1) // 2
    if (r + 1) * 2 <= n + m - 1:
        r += 1
    for i in range(r):
        Q = i
        counter0 = 0
        counter1 = 0
        for j in range(Q + 1):
            if j >= m:
                continue
            if Q - j >= n:
                continue
            if a[Q - j][j] == 0:
                counter0 += 1
            else:
                counter1 += 1
        Q = n + m - 2 - i
        for j in range(Q + 1):
            if j >= m:
                continue
            if Q - j >= n:
                continue
            if a[Q - j][j] == 0:
                counter0 += 1
            else:
                counter1 += 1
        cost += min(counter0, counter1)
    print(cost)
