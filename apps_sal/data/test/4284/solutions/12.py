from math import ceil


q = int(input())

for _ in range(q):
    k, n, a, b = list(map(int, input().split()))

    if b * n >= k:
        print(-1)
    else:
        d = a * n - k + 1
        if d <= 0:
            print(n)
        else:
            r = a - b
            print(n - ceil(d / r))
