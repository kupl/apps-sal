n, k = map(int, input().split())
t = [i + 1 for i in range(2 * n)]
t = t[::-1]
index = t.index(k + 1)
if k > 0:
    if k % 2 == 1:
        for i in range(2 * n - 1, index, -1):
            t[i] = t[i - 1]
        t[index] = 1

    else:
        index = t.index(2 * k)
        for i in range(index, 2 * n - 1, 2):
            t[i], t[i + 1] = t[i + 1], t[i]

for i in range(2 * n):
    print(t[i], end=' ')
