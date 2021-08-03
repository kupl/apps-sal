def __starting_point():

    n, m = [int(x) for x in input().split()]
    f = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    fdict = dict()
    for i, fi in enumerate(f):
        if fi in fdict:
            fdict[fi].append(i)
        else:
            fdict[fi] = [i]

    a = []
    res = "Possible"
    for i, bi in enumerate(b):
        if bi in fdict:
            a_options = fdict[bi]
            a.append(a_options[0])
            if len(a_options) > 1:
                res = "Ambiguity"
        else:
            res = "Impossible"
            break

    print(res)
    if res == "Possible":

        if len(a) != m:
            print("len(a) != m , len(a) =", len(a))

        print(" ".join([str(x + 1) for x in a]))
    elif res == "Ambiguity":

        if len(a) != m:
            print("len(a) != m , len(a) =", len(a))


__starting_point()
