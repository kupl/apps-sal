t = int(input())
for _ in range(t):
    (h, n) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    p.reverse()
    s = n - 1
    c = 0
    l = h
    while 1:
        if l < 3:
            break
        if s < 1:
            break
        if l - p[s - 1] > 1:
            l = p[s - 1] + 1
        elif s < 2:
            if p[s] - 2 > 0:
                c += 1
            break
        elif l - p[s - 2] == 2:
            l = p[s - 2]
            s -= 2
        else:
            c += 1
            l -= 2
            s -= 1
    print(c)
