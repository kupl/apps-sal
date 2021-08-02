def game():
    n = input()
    m = input()
    nlist = []
    mlist = []
    for i in range(len(n)):
        nlist.append(n[i])
    for i in range(len(m)):
        mlist.append(m[i])
    counter = 0
    for i in range(len(m)):
        if not m[i] in n:
            print(-1)
            return 1
    for i in range(len(m)):
        if m[i] in nlist:
            counter += 1
            mlist[i:i + 1] = []
            nlist[nlist.index(m[i])] = []
    print(counter)


game()
