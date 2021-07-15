def main():
    n = int(input().strip())
    aa, bb = [], []
    for _ in range(n):
        a = int(input().strip())
        if a > 0:
            aa.append(a)
        else:
            bb.append(-a)
    res = sum(aa) - sum(bb)
    if res:
        res = res < 0
    else:
        res = a < 0
        aa.append(0)
        bb.append(0)
        for a, b in zip(aa, bb):
            if a != b:
                res = a < b
                break
    print(('first', 'second')[res])


main()
