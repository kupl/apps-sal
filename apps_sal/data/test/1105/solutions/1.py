n = int(input())

m = []
d = dict()

for i in range(n):
    x, k = map(int, input().split())

    if k in d:
        r = d[k]
        if x > r+1:
            print('NO')
            return
        d[k] = max(r, x)
    else:
        if x != 0:
            print('NO')
            return
        d[k] = x

print('YES')
