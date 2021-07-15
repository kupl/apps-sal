for t in range(int(input())):
    a, b, p = [int(i) for i in input().split()]
    s = input()[::-1]
    n = len(s)
    curr = s[1]
    res = 0
    for i in range(1, n):
        if (s[i] != curr):
            if (curr == "A"):
                p -= a
                curr = "B"
            else:
                p -= b
                curr = "A"
            if (p < 0):
                break
            else:
                res = i - 1
    if (curr == "A"):
        p -= a
    else:
        p -= b
    if (p < 0):
        print(n - res)
    else:
        print(1)
