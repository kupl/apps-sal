(n, n1, n2) = [int(x) for x in input().split()]
n3 = 0
a = 0
for i in input().split():
    i = int(i)
    if i == 1:
        if n1:
            n1 -= 1
        elif n2:
            n2 -= 1
            n3 += 1
        elif n3:
            n3 -= 1
        else:
            a += 1
    elif n2:
        n2 -= 1
    else:
        a += 2
print(a)
