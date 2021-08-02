h, w, n = list(map(int, input().split()))
square = dict()
for i in range(n):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    for x in range(b - 2, b + 1, 1):
        for y in range(a - 2, a + 1, 1):
            if 0 <= y <= (h - 3) and 0 <= x <= (w - 3):
                if (x, y) in square:
                    square[(x, y)] += 1
                else:
                    square[(x, y)] = 1
ans = [0 for i in range(10)]
for i in list(square.values()):
    ans[i] += 1
ans[0] = (h - 2) * (w - 2) - sum(ans)
for i in range(10):
    print((ans[i]))
