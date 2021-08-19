def mi():
    return list(map(int, input().split()))


'\n4\n10 2 3 7\n100 51 51 51\n1234 1 100 199\n1000000000 1 1 1000000000\n'
for _ in range(int(input())):
    (L, v, l, r) = mi()
    cl = l
    if cl > v and cl % v:
        cl -= cl % v
        cl += v
    elif cl < v:
        cl = v
    cr = r
    if cr > v:
        cr -= cr % v
    print(max(0, L // v - ((cr - cl) // v + 1)))
