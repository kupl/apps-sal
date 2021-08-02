s = input(); a = 0; b = []
for x in s:
    if x == "(":
        a += 1
    else:
        if x == ")":
            a -= 1
        else:
            a -= 1
            b.append(1)
        if a < 0:
            print(-1)
            return
b[-1] += a;

a = 0; i = 0
for x in s:
    if x == "(":
        a += 1
    else:
        if x == ")":
            a -= 1
        else:
            a -= b[i]; i += 1
        if a < 0:
            print(-1)
            return
if a != 0:
    print(-1)
else:
    for x in b:
        print(x)
