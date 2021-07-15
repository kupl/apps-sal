for _ in range(int(input())):
    a = sorted(list(map(int, input().split())))
    if (a[1] != a[2]):
        print("NO")
    else:
        print("YES")
        print(a[0], a[0], a[2])


