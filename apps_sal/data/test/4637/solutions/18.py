t = int(input())
while t > 0:
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(k):
        if a[0] < b[-1]:
            (a[0], b[-1]) = (b[-1], a[0])
        a.sort()
        b.sort()
    print(sum(a))
    t -= 1
