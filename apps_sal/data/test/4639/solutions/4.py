for tc in range(int(input())):
    (size, pos) = list(map(int, input().split()))
    tl = 1
    tot = 0
    while tot + tl < pos:
        tot += tl
        tl += 1
    res = ['a' for _ in range(size)]
    res[-tl - 1] = 'b'
    res[-(pos - tot)] = 'b'
    print(''.join(res))
