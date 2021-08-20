(q, w, e) = list(map(int, input().split()))
a = list(map(int, input().split()))
z = a.count(1)
x = a.count(2)
r = 0
s = 0
for i in a:
    if i == 1:
        if w > 0:
            w -= 1
        elif e > 0:
            e -= 1
            r += 1
        elif r > 0:
            r -= 1
        else:
            s += 1
    elif e > 0:
        e -= 1
    else:
        s += 2
print(s)
