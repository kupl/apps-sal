for _ in range(int(input())):
    (n, x) = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    (max1, max2) = (-float('inf'), -float('inf'))
    for q in a:
        max1 = max(q[0], max1)
        max2 = max(max2, q[0] - q[1])
    if max1 >= x:
        print(1)
    elif max2 <= 0:
        print(-1)
    else:
        print((x - max1 + max2 - 1) // max2 + 1)
