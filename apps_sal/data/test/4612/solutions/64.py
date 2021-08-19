(a, b) = map(int, input().split())
if (a + b) % 2 == 0:
    print('{:.0f}'.format((a + b) / 2))
else:
    print('{:.0f}'.format((a + b) / 2 - 0.5 + 1))
