t = int(input())
for _ in range(t):

    x, y, a, b = list(map(int, input().split()))
    if (y - x) % (a + b) != 0:
        print(-1)
    else:
        print(int((y - x) / (a + b)))
