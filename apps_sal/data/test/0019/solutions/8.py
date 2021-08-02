for ahfiuyh in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    cc = [0, 0]
    f = True
    for i in a:
        if i[1] > i[0]:
            print("NO")
            f = False
            break
        elif i[0] < cc[0]:
            print("NO")
            f = False
            break
        elif i[1] < cc[1]:
            print("NO")
            f = False
            break
        elif i[1] - cc[1] > i[0] - cc[0]:
            print("NO")
            f = False
            break
        cc = i
    if f:
        print("YES")
