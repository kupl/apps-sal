n = int(input())
for i in range(n):
    k = int(input())
    l = 1000000000000
    r = 0
    for i in range(k):
        (a, b) = list(map(int, input().split()))
        if a > r:
            r = a
        if l > b:
            l = b
    if l >= r:
        print(0)
    else:
        print(r - l)
