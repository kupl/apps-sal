t = int(input())
for q in range(t):
    (h, n) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    s = 0
    i = 1
    while h > 2 and i < n:
        if h - p[i] == 1:
            if i + 1 < n:
                if p[i] - p[i + 1] > 1:
                    s += 1
                    h = p[i] - 1
                    i += 1
                else:
                    h = p[i + 1]
                    i += 2
            elif p[i] == 1:
                h = 0
            else:
                s += 1
                h = p[i] - 1
                i += 1
        else:
            h = p[i] + 1
    print(s)
