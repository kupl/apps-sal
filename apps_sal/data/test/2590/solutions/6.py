for ahfiuyh in range(int(input())):
    (n, x) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = 0
    cc = 0
    f = True
    for i in range(n):
        cc += 1
        s += a[i]
        if s // cc < x:
            print(i)
            f = False
            break
    if f:
        print(n)
