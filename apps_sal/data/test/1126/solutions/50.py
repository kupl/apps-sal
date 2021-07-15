n, x, m = map(int, input().split())

a = [x]
c = [0]*(m+1)
flag = False
for i in range(1, n):
    v = a[i-1]**2 % m
    if c[v] == 1:
        flag = True
        break
    a.append(v)
    c[v] = 1
if flag:
    e = a.index(v)
    s = len(a) - e
    d, f = divmod(n-e, s)
    print(sum(a[:e]) + d*sum(a[e:e+s]) + sum(a[e:e+f]))
else:
    print(sum(a))
