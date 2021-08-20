def __starting_point():
    inp = input()
    arr = inp.split(' ')
    n = int(arr[0])
    m = int(arr[1])
    s = int(arr[2])
    f = int(arr[3])
    ans = ''
    ch = 'L'
    inc = -1
    if s < f:
        ch = 'R'
        inc = 1
    tm = 1
    done = False
    for i in range(m):
        inp = input()
        if done:
            continue
        arr = inp.split(' ')
        ct = int(arr[0])
        l = int(arr[1])
        r = int(arr[2])
        while ct != tm:
            ans += ch
            tm += 1
            s += inc
            if s == f:
                break
        if s != f and (s + inc >= l and s + inc <= r or (s >= l and s <= r)):
            ans += 'X'
        elif s != f:
            ans += ch
            s += inc
        tm += 1
        if s == f:
            done = True
    while s != f:
        s += inc
        ans += ch
    print(ans)


__starting_point()
