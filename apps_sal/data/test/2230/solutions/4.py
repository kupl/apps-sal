n = int(input())
a = int(n ** 2 + 1)
t = 1

for i in range(1, n + 1):
    for j in range(int(n / 2) - 1):
        print('%d %d' % (t, a - t), end=' ')
        t += 1
    print('%d %d' % (t, a - t))
    t += 1
