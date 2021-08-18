q = int(input())
for i in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    p.sort(reverse=True)
    x, a = list(map(int, input().split()))
    y, b = list(map(int, input().split()))
    k = int(input())
    if x < y:
        a, b, x, y = b, a, y, x
    j = min(a, b)
    last_j = 0
    if j == a == b:
        A = 2 * a
        B = 2 * b
        np1 = 0
        np2 = 0
        np3 = 1
        new = "p3"
    elif j == a:
        A = 2 * a
        B = b
        np1 = 1
        np2 = 0
        np3 = 0
        new = "p1"
    else:
        A = a
        B = 2 * b
        np1 = 0
        np2 = 1
        np3 = 0
        new = "p2"
    s = 0
    while j <= n and s < k:
        if new == "p2":
            s += p[np1 + np2 + np3 - 1] / 100 * y
        elif new == "p1":
            s += p[np3 + np1 - 1] / 100 * x
            if np2 > 0:
                s += p[np1 + np2 + np3 - 1] / 100 * y - p[np3 + np1 - 1] / 100 * y
        else:
            s += p[np3 - 1] / 100 * (y + x)
            if np1 > 0:
                s += p[np3 + np1 - 1] / 100 * x - p[np3 - 1] / 100 * x
            if np2 > 0:
                s += p[np1 + np3 + np2 - 1] / 100 * y - p[np1 + np3 - 1] / 100 * y
        last_j = j
        j = min(A, B)
        if j == A == B:
            A += a
            B += b
            np3 += 1
            new = "p3"
        elif j == A:
            A += a
            np1 += 1
            new = "p1"
        else:
            B += b
            np2 += 1
            new = "p2"
    if s >= k:
        print(last_j)
    else:
        print(-1)
