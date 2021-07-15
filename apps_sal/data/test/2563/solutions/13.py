for _ in range(int(input())):
    s = input()
    e = []
    o = []
    for i in s:
        if int(i)%2:
            o.append(int(i))
        else:
            e.append(int(i))
    o.reverse()
    e.reverse()
    ans = []
    while e and o:
        if e[-1] < o[-1]:
            ans.append(e.pop())
        else:
            ans.append(o.pop())
    if e:
        while e:
            ans.append(e.pop())
    else:
        while o:
            ans.append(o.pop())
    print(''.join(map(str, ans)))
