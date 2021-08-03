q = int(input())

for _ in range(q):
    n, m, k = list(map(int, input().split()))
    if k == 0:
        if n == 0 and m == 0:
            print(0)
        else:
            print(-1)
    elif k == 1:
        if max(abs(n), abs(m)) != 1:
            print(-1)
        elif abs(n) == abs(m) == 1:
            print(1)
        else:
            print(0)
    else:
        if max(abs(n), abs(m)) > k:
            print(-1)
        elif abs(n) == abs(m):
            if (k - abs(n)) % 2 == 0:
                print(k)
            else:
                print(k - 2)
        elif (max(abs(n), abs(m)) - min(abs(n), abs(m))) % 2 == 0:
            if (k - max(abs(n), abs(m))) % 2 == 0:
                print(k)
            else:
                print(k - 2)
        else:
            print(k - 1)
