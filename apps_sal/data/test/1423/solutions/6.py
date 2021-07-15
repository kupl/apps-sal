read = lambda: map(int, input().split())
n, l, r = read()
a = list(read())
p = list(read())
d = [i for i in range(n)]
d.sort(key = lambda x: p[x])
cur = l - a[d[0]]
b = [0] * n
for ind in d:
    b[ind] = a[ind] + cur
    if b[ind] < l:
        cur = l - a[ind]
        b[ind] = l
    cur += 1
if max(b) > r: 
    print(-1)
    return
print(' '.join(map(str, b)))
