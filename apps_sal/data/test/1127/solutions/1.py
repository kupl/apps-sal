q = int(input())
for _ in range(q):
    n = int(input())
    s = input()
    s = list(map(int, s))
    r = []
    prz = []
    for i in range(n):
        if i % 2 == 0:
            r.append(s[i] % 2)
        else:
            prz.append(s[i] % 2)
    if n % 2 == 0:
        if prz.count(0) > 0:
            print(2)
        else:
            print(1)
    else:
        if r.count(1) > 0:
            print(1)
        else:
            print(2)
