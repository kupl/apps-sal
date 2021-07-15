def __starting_point():
    inp = input()
    arr = inp.split('+')
    L = []
    for a in arr:
        L.append(int(a))
    L.sort()
    b = False
    ret = ''
    for l in L:
        if b:
            ret+='+'+str(l)
        else:
            ret+=str(l)
            b=True
    print(ret)
        

__starting_point()
