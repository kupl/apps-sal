# ABC135 A

A, B = map(int, input().split())
if (A + B) / 2 % 1 == 0:
    print(int((A + B) / 2))
else:
    print("IMPOSSIBLE")
