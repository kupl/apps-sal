n = int(input())
a = sorted(list(map(int, input().split())))[::-1]
i = 0
if (a[-1] == 5):
    print(-1)
else:
    while (a[i] == 5):
        i += 1
    if (i < 9):
        if (i < n):
            print(0)
        else:
            print(-1)
    else:
        for j in range(i - i % 9):
            print('5', end = '')
        for j in range(n - i):
            print('0', end = '')
