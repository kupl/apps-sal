from sys import stdin as s
for i in range(int(s.readline())):
    a = s.readline().rstrip()
    l = len(a)
    a = int(a)
    c = (l - 1) * 9
    list = [int(str(j) * l) for j in range(1, 10)]
    for j in list:
        if j <= a:
            c += 1
    print(c)
