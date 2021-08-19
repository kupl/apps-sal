O = input()
E = input()
Ans = []
if len(O) - len(E) == 0:
    for i in range(len(O)):
        Ans.append(O[i])
        Ans.append(E[i])
else:
    for i in range(len(E)):
        Ans.append(O[i])
        Ans.append(E[i])
    Ans.append(O[len(O) - 1])
print(''.join(Ans))
