for _ in range(int(input())):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    b.reverse()
    s = sum(a)
    for i in range(k):
        if b[i] - a[i] <= 0:
            break
        s += b[i] - a[i]
    print(s)
