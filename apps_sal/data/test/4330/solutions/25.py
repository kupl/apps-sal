a, b = map(int, input().split())
if (b + a) % 2 == 0:
    print((a + b) // 2)
else:
    print("IMPOSSIBLE")
