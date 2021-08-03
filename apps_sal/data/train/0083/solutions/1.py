t = int(input())
for _ in range(t):
    x, y, a, b = list(map(int, input().split()))
    k = y - x
    if k % (a + b) == 0:
        print(k // (a + b))
    else:
        print(-1)
