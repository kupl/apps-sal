def go():
    n, m = (int(i) for i in input().split(' '))
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    c = []
    for i in b:
        try:
            c.append(a.index(i))
        except:
            continue

    return ' '.join(str(a[i]) for i in sorted(c))


print(go())
