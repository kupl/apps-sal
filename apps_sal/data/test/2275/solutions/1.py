for _ in range(int(input())):
    n = int(input())
    s = input()
    (res, prev) = (0, -1)
    for (i, e) in enumerate(s):
        if e == 'A':
            prev = i
        elif prev != -1:
            res = max(res, i - prev)
    print(res)
