t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    while 1:
        b = a.copy()
        for i in p:
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
        if b == a:
            break
    b = a.copy()
    b.sort()
    if b == a:
        print("YES")
    else:
        print("NO")
