def main():
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list()
    for x in a:
        if x in b:
            b.pop(b.index(x))
        else:
            c.append(x)
    L = 0
    if len(c) == 0:
        return 0
    i = 0
    while len(c):
        while i < len(b) and b[i] < c[0]:
            i += 1
        if i == len(b):
            return len(c)
        b.pop(i)
        c.pop(0)
    return len(c)


print(main())
