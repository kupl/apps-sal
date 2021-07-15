a1, a2 = map(int, input().split())
if (a1 - a2) % 3 == 0:
    if a1 + a2 > 2:
        print(a1 + a2 - 3)
    else:
        print(0)
else:
    print(a1 + a2 - 2)
