O = str(input())
E = str(input())
S = ''
for i in range(len(O) + len(E)):
    if i % 2 == 0:
        S += O[i // 2]
    else:
        S += E[i // 2]
print(S)
