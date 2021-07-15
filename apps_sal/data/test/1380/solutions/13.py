a = input()
a = a.split()
a = list(map(int,a))
n = a[0]
k = a[1]
h = input()
h = h.split()
h = list(map(int,h))
c = []
def make(h,x):
    nonlocal k
    r = list(range(x))
    r.reverse()
    counter = 0
    #print(r)
    for i in r:
        if (h[i+1] - h[i] != k):
            h[i] = h[i+1] - k
            counter += 1
    #print(list(range(x+1,n)))
    for i in range(x+1,n):
        if (h[i] - h[i-1] != k):
            h[i] = h[i-1] + k
            counter += 1
    if (min(h) <= 0):
        counter = 1000000
    return counter
def myPrint(h,x):
    nonlocal k
    #print(h)
    r = list(range(x))
    r.reverse()
    #print(r)
    for i in r:
        if (h[i+1] - h[i] != k):
            if (h[i] < h[i+1] - k):
                print('+',i+1,h[i+1] - k - h[i])
            else:
                print('-',i+1,-(h[i+1] - k - h[i]))
            h[i] = h[i+1] - k
    #print(list(range(x+1,n)))
    for i in range(x+1,n):
        if (h[i] - h[i-1] != k):
            if (h[i] < h[i-1] + k):
                print('+',i+1,h[i-1] + k - h[i])
            else:
                print('-',i+1,-(h[i-1] + k - h[i]))
            h[i] = h[i-1] + k
    return
for i in range(n):
    c.append(make(h.copy(),i))
m = c.index(min(c))
print(c[m])
myPrint(h,m)

