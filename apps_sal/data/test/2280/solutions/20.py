t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
    else:
        max1 = max2 = -1
        for q in a:
            if q > max1:
                max1, max2 = q, max1
            elif q > max2:
                max2 = q
        print(max(0, min(max2 - 1, len(a) - 2)))
