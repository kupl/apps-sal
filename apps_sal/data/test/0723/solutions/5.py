n = int(input())
ar = []
for i in range(n):
    a, b = map(int, input().split())
    ar.append((a, b))
l = 0
hmin = 0
for i in ar:
    hmin = max(hmin, min(i[0], i[1]))
s = 10000000000000
for h in range(hmin, 1001):
    l = 0
    for i in ar:
        if i[0] > h:
            l += i[0]
        elif i[1] > h:
            l += i[1]
        else:
            l += min(i[0], i[1])
            
    s = min(s, l * h)
print(s)
