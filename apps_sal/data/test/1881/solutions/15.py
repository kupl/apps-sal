a = [0 for i in range(0, 256)]
n, k = input().split(' ')
k = int(k)
for c in input().split(' '):
    c = int(c)
    if a[c] != 0:
        print(a[c] - 1, end=' ')
    else:
        for x in range(c, c - k, -1):
            if a[x] == 0:
                i = x
            else:
                if c - a[x] + 1 < k:
                    i = a[x] - 1
                break
            if x == 0:
                break
        for x in range(int(i), c + 1):
            a[x] = i + 1
        print(i, end=' ')
