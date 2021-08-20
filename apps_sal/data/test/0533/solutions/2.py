def main():
    import sys
    input = sys.stdin.readline
    a1 = int(input())
    a2 = int(input())
    k1 = int(input())
    k2 = int(input())
    n = int(input())
    mi = max(0, a1 + a2 - (a1 * k1 + a2 * k2 - n))
    if k1 > k2:
        (a1, a2) = (a2, a1)
        (k1, k2) = (k2, k1)
    ma = 0
    if n >= a1 * k1:
        n -= a1 * k1
        ma += a1
        ma += n // k2
    else:
        ma = n // k1
    print(mi, ma)
    return 0


main()
