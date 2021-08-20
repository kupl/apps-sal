N = int(input())
S = list(input())
L = []
for s in S:
    if len(L) >= 2 and s == 'x':
        if L[-2] == 'f' and L[-1] == 'o':
            L.pop()
            L.pop()
        else:
            L.append(s)
    else:
        L.append(s)
print(len(L))
