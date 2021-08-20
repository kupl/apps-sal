O = input()
E = input()
for i in range(min(len(O), len(E))):
    print(O[i], E[i], sep='', end='')
if len(O) > len(E):
    print(O[-1])
