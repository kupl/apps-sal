t = int(input())

for _ in range(t):
    h, c, g = [int(x) for x in input().split()]
    av = (h + c) / 2
    if g == h:
        print(1)
    elif g <= av + 0.001:
        print(2)
    else:
        n = int((g - h) / (h + c - g * 2))
        best_n = -1
        for j in range(max(n - 3, 0), n + 3):
            if best_n == -1 or \
                    abs(((best_n + 1) * h + best_n * c) - (2 * best_n + 1) * g) * (2 * j + 1) > \
                    abs(((j + 1) * h + j * c) - g * (2 * j + 1)) * (2 * best_n + 1):
                best_n = j
        print(2 * best_n + 1)
