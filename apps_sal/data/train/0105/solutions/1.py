t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    ct = 0

    for i in range(1, n):
        ct += (k - a[i]) // a[0]

    print(ct)
