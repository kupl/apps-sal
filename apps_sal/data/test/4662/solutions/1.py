maxdepth = 0
def depth(elem, level):
    #print(elem)
    if level == -1:
        level = 0
    nonlocal maxdepth
    if level > maxdepth:
        maxdepth = level
    for el in elem:
        depth(el, level+1)


