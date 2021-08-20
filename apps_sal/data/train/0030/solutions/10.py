for _ in range(int(input())):
    n = int(input())
    s = input()
    l = list(s)
    c0 = 0
    c1 = 0
    for i in range(n - 1):
        if l[i] == l[i + 1]:
            if l[i] == '0':
                c0 += 1
            else:
                c1 += 1
    print(max(c0, c1))
