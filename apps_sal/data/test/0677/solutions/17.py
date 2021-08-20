def mi():
    return list(map(int, input().split()))


'\n5\n2 4 2\n5 10 4\n3 10 1\n1 2 3\n4 6 5\n'
for _ in range(int(input())):
    (l, r, d) = mi()
    nl = d
    nr = r - r % d
    nr += d
    if nl < l:
        print(nl)
    else:
        print(nr)
