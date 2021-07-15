# map(int, input().split())
rw = int(input())
for wewq in range(rw):
    n = int(input())
    a = 0
    b = 0
    c = 0
    if n % 3 == 0:
        print(n // 3, 0, 0)
    elif n % 3 == 1:
        if n // 3 - 2 < 0:
            print(-1)
            continue
        print(n // 3 - 2, 0, 1)
    elif n % 3 == 2:
        if n // 3 - 1 < 0:
            print(-1)
            continue
        print(n // 3 - 1, 1, 0)


