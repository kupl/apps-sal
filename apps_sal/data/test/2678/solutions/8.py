n = int(input())
c = []
m = n
while(n > 0):
    a, b = input().split()
    a = int(a)
    b = int(b)
    c.append([a, b])
    n = n - 1
c.sort()
f = 0
s = 1
total = 1
while(f < m - 1):
    while(s < m):
        if(c[f][1] < c[s][0]):
            total = total + 1
            f = s
            s = s + 1
        elif((c[f][1] >= c[s][0]) and (c[f][1] >= c[s][1])):
            f = s
            s = s + 1
        else:
            s = s + 1
    f = f + 1

print(total)
