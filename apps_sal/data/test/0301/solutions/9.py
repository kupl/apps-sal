XOR, SUM = map(int, input().split())
if XOR > SUM or XOR % 2 != SUM % 2:
    print(-1)
elif SUM == 0:
    print(0)
elif XOR == SUM:
    print(1)
    print(SUM)
else:
    a = (SUM - XOR) // 2
    if (a ^ XOR) == a + XOR:
        print(2)
        print(a ^ XOR, a)
    else:
        print(3)
        print(a, a, XOR)
