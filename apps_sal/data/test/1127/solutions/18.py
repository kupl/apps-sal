t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    R = []
    B = []
    for i in range(n):
        t = int(s[i])
        t %= 2
        if i % 2 == 0:
            R.append(t)
        else:
            B.append(t)
    R = set(R)
    B = set(B)
    if n % 2 == 1:
        if 1 in R:
            print(1)
        else:
            print(2)
    else:
        if 0 in B:
            print(2)
        else:
            print(1)
