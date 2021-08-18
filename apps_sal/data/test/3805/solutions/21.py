X = input()
L = []
for i in X:
    if L == []:
        L.append(str(i))
    else:
        if i == L[len(L) - 1]:
            L.pop()
        else:
            L.append(i)
if L == []:
    print('Yes')
else:
    print('No')
