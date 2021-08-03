n = int(input())
l = input().split()
s = 0
for i in range(n):
    l[i] = int(l[i])
    s += l[i]
if(s % n == 0):
    q = s // n
    r = 0
    for i in range(n):
        if(l[i] > q):
            r += l[i] - q
    print(r)
else:
    p = s % n
    q = (s - s % n) // n
    r = 0
    l.sort()
    l.reverse()
    for i in range(n):
        if(i < p):
            if(l[i] > q + 1):
                r += l[i] - q - 1
        else:
            if(l[i] > q):
                r += l[i] - q
    print(r)
