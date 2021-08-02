for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    t = 0
    for i in range(1, n):
        if a[i] < a[i - 1]:
            t += a[i - 1] - a[i]
    print(t)
