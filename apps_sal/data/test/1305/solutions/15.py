def main():
    n = int(input())
    L = [int(x) for x in input().split()]
    q, h = 0, 0
    for p in L:
        if p == 25:
            q += 1
        elif p == 50:
            if q > 0:
                h += 1
                q -= 1
            else:
                return 'NO'
        else:
            if q > 0 and h > 0:
                q -= 1
                h -= 1
            elif q > 2:
                q -= 3
            else:
                return 'NO'
    return 'YES'


print(main())
