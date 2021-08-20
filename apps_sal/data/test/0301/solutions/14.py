(a, b) = list(map(int, input().split()))
if a > b or (b - a) % 2 != 0:
    print(-1)
else:
    k = b - a
    if k == 0:
        if a == 0:
            print(0)
        else:
            print(1, '\n' + str(a))
    elif a & k // 2 == 0:
        print(2)
        print(a + k // 2, k // 2)
    else:
        print(3)
        print(a, k // 2, k // 2)
