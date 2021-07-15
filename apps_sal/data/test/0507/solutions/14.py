n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0]*n
d = [False]*n
bad = []
need = []
for i in range(n):
    if a[i] == b[i]:
        d[a[i]-1] = True
        c[i] = a[i]
    else:
        bad.append(i)
for i in range(n):
    if not d[i]:
        need.append(i+1)

d = False

def good(c):
    nonlocal a, b
    al = 0
    bl = 0
    for i in range(len(c)):
        if c[i] != a[i]:
            al += 1
        if c[i] != b[i]:
            bl += 1
    if al == 1 and bl == 1:
        for i in range(len(c)):
            for j in range(len(c)):
                if i != j and c[i] == c[j]:
                    return False
    else:
        return False
    return True
fc = []
do = False
def f(b, n, c):
    nonlocal do, fc
    #print(b, n, c, do)
    if not do:
        if len(b) == 0 and good(c):
            do = True
            fc = c
            #print(fc)
        else:
            for i in range(len(b)):
                for j in range(len(n)):
                    nc = c+[]
                    nc[b[i]] = n[j]
                    f(b[:i]+b[i+1:]+[], n[:j]+n[j+1:]+[], nc)

f(bad, need, c)
for i in fc:
    print(i ,end=' ')
