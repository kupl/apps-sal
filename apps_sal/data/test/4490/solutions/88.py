AT = ['A', 'T']
CG = ['C', 'G']
b = input()

if b in AT:
    AT.remove(b)
    print((*AT))
else:
    CG.remove(b)
    print((*CG))
