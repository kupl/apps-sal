a = list(input())
b = list(input())
c = list(input())

A = len(a)
B = len(b)
C = len(c)
cnta = 0
cntb = 0
cntc = 0
for i in range(A + B + C):
    if i == 0:
        cnta += 1
        if cnta > A:
            print("A")
            break
        q = a[0]
        a.pop(0)
        continue
    if q == "b":
        cntb += 1
        if cntb > B:
            print("B")
            break
        q = b[0]
        b.pop(0)

    elif q == "a":
        cnta += 1
        if cnta > A:
            print("A")
            break
        q = a[0]
        a.pop(0)

    else:
        cntc += 1
        if cntc > C:
            print("C")
            break
        q = c[0]
        c.pop(0)
