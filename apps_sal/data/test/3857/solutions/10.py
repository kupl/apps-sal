def main():
    mode = "filee"
    if mode == "file":
        f = open("test.txt", "r")

    def get(): return [int(x) for x in (f.readline() if mode == "file" else input()).split()]
    [n] = get()
    a = get()
    a.sort()
    p = [[]]
    p[0].append(a[0])
    for i in a[1:]:
        p = sorted(p, key=lambda x: len(x))
        p.reverse()
        found = False
        for j in p:
            if len(j) <= i:
                j.append(i)
                found = True
                break
        if found == False:
            p.append([i])
    print(len(p))

    if mode == "file":
        f.close()


def __starting_point():
    main()


__starting_point()
