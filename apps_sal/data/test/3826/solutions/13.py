def f(m):
    b = {}
    for i in a[m:]:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    #print(m,b)
    k = 0
    for i in b:
        if b[i] > 1:
            k += 1
    if k == 0:
        return True
    for i in range(n-m):
        b[a[i+m]] -= 1
        if b[a[i+m]] == 1:
            k -= 1
        if a[i] in b:
            b[a[i]] += 1
            if b[a[i]] == 2:
                k += 1
        else:
            b[a[i]] = 1
        if k == 0:
            return True
    return False

n = int(input())
a = list(map(int,input().split()))

l = 0
r = n
while r-l > 1:
    m = (r+l)//2
    if f(m):
        r = m
    else:
        l = m
if f(l):
    r = l
print(r)

