n, t = map(int, input().strip().split())
mn = 10000000
num = 0
for i in range(n):
    s,d = map(int, input().strip().split())
    temp = 0
    if s >= t:
        temp= s - t
    else:
        g = t - s
        md = g % d
        if md != 0:
            temp = d - md
        else:
            temp = 0
    if temp < mn:
        mn = temp
        num = i+1
print(num)
