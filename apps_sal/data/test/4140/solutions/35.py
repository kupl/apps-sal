S = input()

N = len(S)
O, E = 0, 0
for i, s in enumerate(S):
    O += (i % 2) ^ int(s)
    E += (i % 2) ^ (not int(s))
print(min(O, E))
