for _ in range(int(input())):
    int(input())
    a = list(map(int, input().split()))

    b = []
    for i in range(0, len(a), 2):
        b.append(-a[i + 1])
        b.append(a[i])

    print(*b)

