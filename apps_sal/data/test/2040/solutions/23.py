t = [0] * 400
x = k = 0
for q in range(int(input())):
    y = int(input())
    d, x = y - x, y
    j = 0
    while d < 1 or t[j] > min(8, 9 * j + 9 - d):
        d += t[j]
        t[j] = 0
        j += 1
    t[j] += 1
    k = max(k, j)
    a, b = divmod(d - 1, 9)
    t[:a] = [9] * a
    t[a] += b
    print(''.join(map(str, t[k::-1])))

