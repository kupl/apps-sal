(L, R) = list(map(int, input().split()))
'\nR ????????1??????\ny 0001????0??????\n     ^d   ^rd\nx 0001???????1??\n             ^ld\nL ???????????0???\n'
ans = 0
for d in range(70):
    if d < len(bin(L)) - 3:
        LD = []
    elif d == len(bin(L)) - 3:
        LD = [i for i in range(-1, d) if i == -1 or L >> i & 1 == 0]
    else:
        LD = [d]
    if d < len(bin(R)) - 3:
        RD = [d]
    elif d == len(bin(R)) - 3:
        RD = [i for i in range(-1, d) if i == -1 or R >> i & 1 == 1]
    else:
        RD = []
    for ld in LD:
        for rd in RD:
            a = 1
            for i in range(d):
                if i < ld and i < rd:
                    a *= 3
                if i < ld and i == rd:
                    a *= 1
                if i < ld and i > rd:
                    a *= (R >> i & 1) + 1
                if i == ld and i < rd:
                    a *= 1
                if i == ld and i == rd:
                    a *= 0
                if i == ld and i > rd:
                    a *= R >> i & 1
                if i > ld and i < rd:
                    a *= 2 - (L >> i & 1)
                if i > ld and i == rd:
                    if L >> i & 1 == 0:
                        a *= 1
                    else:
                        a *= 0
                if i > ld and i > rd:
                    if L >> i & 1 == R >> i & 1:
                        a *= 1
                    if L >> i & 1 == 0 and R >> i & 1 == 1:
                        a *= 1
                    if L >> i & 1 == 1 and R >> i & 1 == 0:
                        a *= 0
            ans += a
print(ans % (10 ** 9 + 7))
