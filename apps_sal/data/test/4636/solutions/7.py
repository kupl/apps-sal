t = int(input())
for i in range(t):
    n = int(input())
    A = [int(x) for x in input().split()]
    x = A[0]
    l = 1
    r = n - 1
    a = x
    b = 0
    p = 1
    while l <= r:
        p += 1
        c = 0
        while c <= x and l <= r:
            c += A[r]
            r -= 1
        b += c
        if c <= x or l > r:
            break
        x = c
        p += 1
        c = 0
        while c <= x and l <= r:
            c += A[l]
            l += 1
        a += c
        if c <= x or l > r:
            break
        x = c
    print(p, a, b)
