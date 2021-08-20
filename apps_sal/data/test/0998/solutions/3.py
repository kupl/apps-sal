def main():
    buf = input()
    buflist = buf.split()
    n = int(buflist[0])
    x = int(buflist[1])
    npow2 = int(2 ** n)
    if n == 1:
        if x == 1:
            print(0)
        else:
            print(1)
            print(1)
        return
    mask = x
    if x >= npow2:
        mask = 0
    available = set()
    for i in range(1, npow2):
        if i != x:
            available.add(i)
    a = []
    while available:
        new_elem = available.pop()
        new_elem = new_elem ^ mask
        a.append(new_elem)
        if x < npow2:
            elem_to_remove = new_elem ^ x
            available.remove(elem_to_remove ^ mask)
        mask = mask ^ new_elem
    print(len(a))
    print(' '.join(list(map(str, a))))


def __starting_point():
    main()


__starting_point()
