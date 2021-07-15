q = int(input())

for i in range(q):
    n, m, k = map(int, input().split())
    p = min(m, n)
    r = max(n, m) - p
    if (p+r) > k:
        print(-1)
    elif r % 2 == 1:
        print(k - 1)
    elif (k - p) % 2 == 0:
        print(k)
    else:
        print(k - 2)
