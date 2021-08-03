q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    t = False
    for i in range(1, n):
        if a[i] - 1 == a[i - 1]:
            t = True
    if t:
        print(2)
    else:
        print(1)
