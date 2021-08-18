def __starting_point():
    inp = input()
    inp = input()
    arr = inp.split(" ")
    Li = []
    Ls = []
    for a in arr:
        Li.append(int(a))

    Li.sort()
    fst = Li.pop(0)
    lst = Li.pop(-1)
    ans = str(lst)
    for x in Li:
        Ls.append(str(x))
    for s in Ls:
        ans += " " + s
    ans += " " + str(fst)
    print(ans)


__starting_point()
