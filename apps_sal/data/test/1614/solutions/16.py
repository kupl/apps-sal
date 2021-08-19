(n, h) = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
w = len(L)
for i in L:
    if i > h:
        w += 1
print(w)
