n = int(input())
b = sorted(list(map(int, input().split())))
if b[n - 1] == b[0]:
    print(0, n * (n - 1) // 2)
else:
    p1, p2, l, r = 1, 1, 0, n - 1
    while b[l] == b[l + 1]:
        p1, l = p1 + 1, l + 1
    while b[r] == b[r - 1]:
        p2, r = p2 + 1, r - 1
    print(b[n - 1] - b[0], p1 * p2)
