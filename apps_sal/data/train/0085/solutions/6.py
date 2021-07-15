for t in range(int(input())):
    s = [int(c == "1") for c in input()]
    x = int(input())
    n = len(s)

    sat = lambda i: (s[i] if i in range(n) else 1)

    w = [(sat(i - x) & sat(i + x)) for i in range(n)]

    wat = lambda i: (w[i] if i in range(n) else 0)

    s_ref = [(wat(i - x) | wat(i + x)) for i in range(n)]
    
    if s != s_ref:
        print(-1)
    else:
        print("".join(map(str, w)))

