O = input()
E = input()
o = len(O)
e = len(E)
[print(O[i], E[i], sep='', end='') for i in range(min(o, e))]
print('' if o == e else O[-1])
