from itertools import product
S = input()
total = 0
length = len(S)
List = list(product([0, 1], repeat=length - 1))
formula = ''
for item in List:
    formula = S[0]
    for i in range(length - 1):
        if item[i] == 0:
            formula += S[i + 1]
        else:
            formula += '+' + S[i + 1]
    total += eval(formula)
print(total)
