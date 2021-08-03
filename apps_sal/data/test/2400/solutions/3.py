def mi():
    return list(map(int, input().split()))


'''
3
3
1 3 2
2
0 3
1
1
1
1
1
2
1
1
'''
for _ in range(int(input())):
    n = int(input())
    a = list(mi())
    m = int(input())
    b = list(mi())

    oa, ob, ea, eb = 0, 0, 0, 0
    for i in a:
        if i % 2:
            oa += 1
        else:
            ea += 1
    for i in b:
        if i % 2:
            ob += 1
        else:
            eb += 1

    print(ea * eb + oa * ob)
