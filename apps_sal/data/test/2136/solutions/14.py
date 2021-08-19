def testcase():
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(input())
    (s1, s2) = (grid[0][1], grid[1][0])
    (f1, f2) = (grid[-1][-2], grid[-2][-1])
    if s1 == s2:
        if f1 == f2:
            if s1 == f1:
                print(2)
                print(1, 2)
                print(2, 1)
                return
            else:
                print(0)
                return
        else:
            if s1 == f1:
                print(1)
                print(n, n - 1)
                return
            if s2 == f2:
                print(1)
                print(n - 1, n)
                return
    elif f1 == f2:
        if s1 == f1:
            print(1)
            print(1, 2)
            return
        if s2 == f2:
            print(1)
            print(2, 1)
            return
    else:
        x = s2
        print(2)
        print(2, 1)
        if f1 == x:
            print(n - 1, n)
        else:
            print(n, n - 1)
    return


t = int(input())
for _ in range(t):
    testcase()
