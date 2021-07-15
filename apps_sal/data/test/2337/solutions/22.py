R = lambda:list(map(int,input().split()))
n,m = R()
a = R()
b = R()
r = 0
for x in a:
    c = 0
    for y in b:
        if y>=x:
            c = 1
            b.pop(b.index(y))
            break
    if c == 0:
        r += 1
print(r)
