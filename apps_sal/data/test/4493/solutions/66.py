c = [[int(x) for x in input().split()] for _ in range(3)]

ans = False
for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            ok = True
            b1 = c[0][0] - a1
            b2 = c[0][1] - a1
            b3 = c[0][2] - a1
            if c[1][0] != a2 + b1 or \
               c[1][1] != a2 + b2 or \
               c[1][2] != a2 + b3 or \
               c[2][0] != a3 + b1 or \
               c[2][1] != a3 + b2 or \
               c[2][2] != a3 + b3:
                ok = False
            if ok:
                ans = True

if ans:
    print("Yes")
else:
    print("No")
