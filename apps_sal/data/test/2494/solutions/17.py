def solve(K):
    checked = [False] * K

    def calc(x):
        while not checked[x]:
            checked[x] = True
            yield x
            x = (x * 10) % K
    i = 0
    xs = [0]
    while 1:
        i += 1
        ys = []
        for x in xs:
            for z in calc((x + 1) % K):
                if z == 0:
                    return i
                ys.append(z)
        xs = ys


K = int(input())
print(solve(K))
