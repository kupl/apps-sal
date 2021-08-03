
t = int(input())
for nt in range(t):
    n = int(input())
    a = [None] * n
    tc = []
    d = set()
    for i in range(n):
        a[i] = input()
        if a[i] in d:
            tc += [i]
        d.add(a[i])
    for i in tc:
        for j in range(10):
            if a[i][:3] + str(j) not in d:
                a[i] = a[i][:3] + str(j)
                d.add(a[i])
                break
    print(len(tc))
    for i in a:
        print(i)
