(n, k) = map(int, input().split())

if k != n:
    s = input()

    d = {}
    for x in s:
        if not x in d:
            d[x] = 0
        d[x] += 1

    lst = sorted(d.keys())

    x = 0
    while x < len(lst):
        if d[lst[x]] > k:
            i = k
            b = lst[x]
            break
        else:
            k -= d[lst[x]]
            x += 1

    acc = 0
    for x in s:
        if x == b:
            acc += 1
            if acc > k:
                print(x, end='')
        elif x > b:
            print(x, end='')
    

