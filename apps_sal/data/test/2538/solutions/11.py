n = int(input())
for i in range(n):
    a, b, c = [int(x) for x in input().split()]
    l = 0
    r = c
    while r - l > 1:
        mid = (l + r) // 2
        if a + mid > b + c - mid:
            r = mid
        else:
            l = mid
    if a > b + c:
        print(c + 1)
    elif a + r > b + c - r:
        print(c - r + 1)

    else:
        print(0)
