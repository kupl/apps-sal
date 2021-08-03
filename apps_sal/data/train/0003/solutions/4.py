for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(1, k + 1):
        a[0] += a[i]
        a[i] = 0
    print(a[0] - a[1])
