for f in range(int(input())):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    x = 0
    while x < k and a[x] < b[x]:
        a[x] = b[x]
        x += 1
    print(sum(a))
