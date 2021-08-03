for _ in range(int(input())):
    s = input()
    n = len(s) - 1
    k = 0
    a = []
    for x in s:
        if x != "0":
            k += 1
            a.append(x + "0" * n)
        n -= 1
    print(k)
    print(*a)
