# HEY STALKER
for _ in range(int(input())):
    n = int(input())
    if n <= 3:
        print(-1)
    else:
        k = []
        for t in range(n, 0, -2):
            k.append(t)
        l = []
        for t in range(n - 3, 0, -2):
            l.append(t)
        l.insert(1, n - 1)
        l.reverse()
        print(*l, *k)
