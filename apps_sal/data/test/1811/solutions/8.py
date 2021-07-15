def s():
    [n,k] = list(map(int,input().split()))
    d = [0]*(n+2)
    c = 2
    d[1] = 1
    for ch in input():
        d[c] = d[c-1]
        if ch == '.' and d[max(0,c-k-1)] != d[c]:
            d[c] += 1
        c += 1
    print('YES' if d[-1] != d[-2] else 'NO')
s()

