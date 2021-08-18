for _ in range(int(input())):
    a, b = map(int, input().split())
    s = input()
    n = len(s)
    j = 0
    while j < n and s[j] == '0':
        j += 1
    c = 0
    r = a
    if j == n:
        r = 0
    damp = 0
    for i in range(j, n):
        if s[i] == '1':
            if damp > 0:
                r += min(a, damp * b)
            damp = 0
        else:
            damp += 1
    print(r)
