n = int(input())
a = list(map(int, input().split()))
a += a
t = 0
maxt = 0
for e in a:
    if e == 1:
        t += 1
        if t > maxt:
            maxt = t
    else:
        t = 0
print(maxt)

