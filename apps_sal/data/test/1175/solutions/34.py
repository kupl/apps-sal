L, R = list(map(int, input().split()))

"""
R ????????1??????
y 0001????0??????
     ^d   ^rd
x 0001???????1??
             ^ld
L ???????????0???
"""

ans = 0

for d in range(70):
    if d < len(bin(L)) - 3:
        LD = []
    elif d == len(bin(L)) - 3:
        LD = [i for i in range(-1, d) if i == -1 or (L >> i & 1) == 0]
    else:
        LD = [d]
    if d < len(bin(R)) - 3:
        RD = [d]
    elif d == len(bin(R)) - 3:
        RD = [i for i in range(-1, d) if i == -1 or (R >> i & 1) == 1]
    else:
        RD = []
    for ld in LD:
        for rd in RD:
            a = 1
            for i in range(d):
                if i < ld:
                    xc = [0, 1]
                elif i == ld:
                    xc = [1]
                else:
                    xc = [L >> i & 1]
                if i < rd:
                    yc = [0, 1]
                elif i == rd:
                    yc = [0]
                else:
                    yc = [R >> i & 1]
                c = 0
                for x in xc:
                    for y in yc:
                        if y >= x:
                            c += 1
                a *= c
            ans += a
print(ans % (10**9 + 7))
