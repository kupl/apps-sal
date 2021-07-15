q = int(input())
for i in range(q):
    n = int(input())
    s = 0
    i = -1
    while s < n:
        i += 1
        s += 3 ** i
    if s == n:
        print(s)
    else:
        for j in range(i, -1, -1):
            if s - 3 ** j >= n:
                s -= 3 ** j
        print(s)
