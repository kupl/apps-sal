#603_C

t = int(input())

for i in range(0, t):
    n = int(input())
    ln = [0]
    oned = False
    sqt = n // int(n ** 0.5)
    on = -1
    for j in range(1, max(2, int(n ** 0.5) + 1)):
        if n // j != on:
            ln.append(n // j)
            if n // j == 1:
                oned = True
        on = n // j
    for j in range(len(ln) - 1, 0, -1):
        if n // ln[j] == sqt:
            continue
        ln.append(n // ln[j])
        if n // ln[j] == 1:
            oned = True
    if not oned:
        ln.append(1)
    print(len(ln))
    print(" ".join([str(j) for j in sorted(ln)]))

