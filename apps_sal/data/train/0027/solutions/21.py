k = int(input())


def absolute():
    c = dict()
    m = 0
    for i in [int(x) for x in input().split()]:
        q = 0
        if i % 2 != 0:
            continue
        while i % 2 == 0:
            i //= 2
            q += 1
        if c.get(i, 0) < q:
            m += q - c.get(i, 0)
            c[i] = q
    # print(c)
    return m


for j in range(k):
    input()
    print(absolute())
