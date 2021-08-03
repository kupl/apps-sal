for _ in range(int(input())):
    n = int(input())
    a = []
    f = 0
    for i in range(n):
        l, r = map(int, input().split())
        a.append([l, r, i])
    a.sort(key=lambda x: x[0])
    rm = a[0][1]
    for i in range(n):
        if a[i][0] > rm:
            b = a[i]
            f = 1
            break
        if a[i][1] > rm:
            rm = a[i][1]
    if f == 0:
        print(-1)
    else:
        a.sort(key=lambda x: x[2])
        for i in range(n):
            if a[i][0] < b[0]:
                print(1, end=" ")
            else:
                print(2, end=" ")
    print()
