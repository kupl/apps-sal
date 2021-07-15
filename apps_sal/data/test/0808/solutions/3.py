# You lost the game.
x = str(input())
n = len(x)
d = 0
while d < n and x[d] == "0":
    d += 1
f = n-1
while f >= 0 and x[f] == "0":
    f -= 1
f += 1
e = x.count(".")
if x.count("0") >= n-1 and e:
    print(0)
elif x[d] == ".":
    i = d+1
    while x[i] == "0":
        i += 1
    if f == i+1:
        print(x[i]+"E"+str(d-i))
    else:
        print(x[i]+"."+x[i+1:f]+"E"+str(d-i))
elif x[f-1] == ".":
    i = f-2
    while x[i] == "0":
        i -= 1
    if d+1 == i+1:
        if f-d-2:
            print(x[d]+"E"+str(f-d-2))
        else:
            print(x[d])
    else:
        print(x[d]+"."+x[d+1:i+1]+"E"+str(f-d-2))
elif e == 0:
    if d == f-1:
        if n-d-1:
            print(x[d]+"E"+str(n-d-1))
        else:
            print(x[d])
    else:
        print(x[d]+"."+x[d+1:f]+"E"+str(n-d-1))
elif x.index(".")-d == 1:
    print(x[d:f])
else:
    e = x.index(".")
    print(x[d]+"."+x[d+1:e]+x[e+1:f]+"E"+str(e-d-1))
    

