C, Pr, Pb, Wr, Wb = list(map(int, input().split()))
result = 0
if Wr * Wr >= C:
    i = 0
    while Wr * i <= C:
        j = int((C - Wr * i) / Wb)
        result = max(result, Pr * i + Pb * j)
        i += 1
    print(result)
    return

if Wb * Wb >= C:
    i = 0
    while Wb * i <= C:
        j = int((C - Wb * i) / Wr)
        result = max(result, Pb * i + Pr * j)
        i += 1
    print(result)
    return

Ab = Pb / Wb
Ar = Pr / Wr

if Ab < Ar:
    i = 0
    while i * i <= C:
        j = int((C - Wb * i) / Wr)
        result = max(result, Pb * i + Pr * j)
        i += 1
    print(result)
else:
    i = 0
    while i * i <= C:
        j = int((C - Wr * i) / Wb)
        result = max(result, Pr * i + Pb * j)
        i += 1
    print(result)

