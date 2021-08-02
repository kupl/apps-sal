t = int(input())
for i in range(t):
    n = int(input())
    s = 0
    for j in range(1, (n + 1) // 2):
        s += j * ((2 * j + 1) * 4 - 4)
    print(s)
