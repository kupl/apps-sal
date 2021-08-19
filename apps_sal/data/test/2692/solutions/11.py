t = int(input())
for _ in range(t):
    n, b = list(map(int, input().split()))
    low = 1
    high = n
    if b == 1:
        print(1)
        continue
    while low < high and abs(high - low) > 4:

        mid = (low + high) // 2
        a = mid // b
        aa = mid % b
        d = mid
        while a:
            #   print(a,aa)
            d += a
            tt = a + aa
            a = tt // b
            aa = tt % b
        if d >= n:
            high = mid
        if d < n:
            low = mid + 1

    for mid in range(low, high + 1):
        a = mid // b
        aa = mid % b
        d = mid
        while d < n and a:
            d += a
            tt = a + aa
            a = tt // b
            aa = tt % b
        if d >= n:
            tt = mid
            break
    print(tt)
