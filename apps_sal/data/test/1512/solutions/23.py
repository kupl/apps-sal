n = int(input())
d = {}
a = list(map(int,input().split()))
if n == 1:
    print(a[0])
elif n == 2:
    print(min(a[0],a[1]))
else:
    for i in a:
        d[i] = 0
    t = [max(a[0],a[1]),min(a[0],a[1])]
    if a[1] > a[0]:
        d[a[1]] -= 1
        d[a[0]] -= 1
    for i in a[2:]:
        if i > t[0]:
            t = [i,t[0]]
            d[i] -= 1
        elif i > t[1]:
            d[t[0]] += 1
            t = [t[0],i]
    a,b = -2,n+1
    for i in d:
        if d[i] > a:
            a = d[i]
            b = i
        elif d[i] == a:
            if i < b:
                b = i
    print(b)
