q = int(input())
for i in range(q):
    (n, m, k) = list(map(int, input().split()))
    (m, n) = (abs(m), abs(n))
    mx = max(m, n)
    remaining = k - mx
    if remaining < 0:
        print(-1)
    elif m == n == 0:
        if k == 1:
            print(-1)
        elif k % 2:
            print(k - 1)
        else:
            print(k)
    elif abs(m - n) % 2 == 0:
        if remaining % 2 == 0:
            print(k)
        else:
            print(k - 2)
    elif not remaining:
        print(k - 1)
    elif remaining % 2 == 0:
        print(k - 1)
    else:
        print(k - 1)
