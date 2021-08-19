t = int(input())
for _ in range(t):
    (n, u) = map(int, input().split())
    a = list(map(int, input().split()))
    k = u // 2
    p = [-1 for i in range(n)]
    if u % 2 != 0:
        for i in range(n):
            if a[i] <= k:
                p[i] = 0
            else:
                p[i] = 1
    else:
        x = 0
        for i in range(n):
            if a[i] < k:
                p[i] = 0
            elif a[i] > k:
                p[i] = 1
            elif a[i] == k:
                if x == 0:
                    p[i] = 0
                    x = 1
                else:
                    p[i] = 1
                    x = 0
    print(*p)
