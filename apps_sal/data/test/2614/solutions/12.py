for _ in range(int(input())):
    n = int(input())
    x = [0] * n
    l = list(map(int, input().split()))
    for i in l:
        x[i - 1] += 1
    x.sort()
    x.reverse()
    m = x[0]
    ap = 0
    for i in x:
        if i == m:
            ap += 1
        else:
            break
    print((n - ap) // (m - 1) - 1)
