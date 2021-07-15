for i in range(int(input())):
    t = input()[4:]
    q, d = int(t), 10 ** len(t)
    while q < 1988 + d // 9: q += d
    print(q)

