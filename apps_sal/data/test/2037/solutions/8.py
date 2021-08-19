(n, m) = map(int, input().split())
arr = [int(x) for x in input().split()]
d = {}
for i in range(1, n + 1):
    d[i] = 0
tmp = set()
for i in arr:
    d[i] += 1
    tmp.add(i)
    if len(tmp) == n:
        print('1', end='')
        for i in d:
            d[i] -= 1
        tmp = set()
        for i in d:
            if d[i] > 0:
                tmp.add(i)
    else:
        print('0', end='')
