s = int(input())
L = []
n = 1
while not s in L:
    L.append(s)
    if s % 2 == 0:
        s //= 2
    else:
        s = s * 3 + 1
    n += 1
print(n)
