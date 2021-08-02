q = int(input())
while(q):
    q -= 1
    n = int(input())
    *a, = map(int, input().split())
    u = [False for i in range(n + 1)]
    u[0] = True
    for i in range(1, n + 1):
        for j in range(n):
            if a[j] == i:
                x = j
                while not u[x] and a[x] < a[x - 1]:
                    a[x], a[x - 1] = a[x - 1], a[x]
                    u[x] = True
                    x -= 1
    print(*a)
