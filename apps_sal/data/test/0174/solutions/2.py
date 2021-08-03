def f(a):
    if len(a) == 1:
        if a[0] == 0:
            print("YES\n0")
            return
        else:
            print("NO")
            return
    if a[-1] == 1:
        print("NO")
        return
    if a[-2] == 1:
        print("YES")
        print("->".join(str(x) for x in a))
        return
    elif len(a) == 2:
        print("NO")
        return
    elif len(a) >= 3 and a[-3] == 0:
        a[-3] = '(0'
        a[-2] = '0)'
        print("YES\n" + "->".join(str(x) for x in a))
        return
    for i in range(len(a) - 3, -1, -1):
        if a[i] == 0:
            a[i] = '(' + str(a[i])
            a[i + 1] = '(' + str(a[i + 1])
            a[-2] = '0))'
            print("YES\n" + "->".join(str(x) for x in a))
            return
    print("NO")
    return


n = int(input())
a = list(int(x) for x in input().split())
f(a)
