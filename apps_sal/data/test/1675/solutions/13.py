def ret(n):
    if n in col:
        return(col[n])
    else:
        return(0)


n = int(input())
col = {}
t = []
for i in range(n):
    a = input().split()
    t.append([n - 1, a[1]])
    if a[0] not in col:
        col[a[0]] = 1
    else:
        col[a[0]] += 1

print('\n'.join('%d %d' % (x[0] + ret(x[1]), (n - 1) - ret(x[1])) for x in t))
