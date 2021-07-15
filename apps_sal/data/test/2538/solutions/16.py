for _ in range(int(input())):
    
    s, i, e = map(int, input().split())
    
    lo, hi, res = 0, e, 0

    if s + e <= i:
        print(0)
        continue

    while lo <= hi:

        mi = (lo + hi) // 2

        if s + mi > i + (e - mi):
            res = mi
            hi = mi - 1
        else:
            lo = mi + 1
    
    print(e - res + 1)
