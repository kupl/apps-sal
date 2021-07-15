q = int(input())
for i in range(q):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    f = False
    for i in range(n - 1):
        if a[i] - a[i + 1] == -1:
            print(2)
            f = True
            break
    if not f:
        print(1)

