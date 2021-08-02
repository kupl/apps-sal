S = input()
T = input()
SS = len(S)
TT = len(T)
hantei = 0
count = 0

if SS + 1 == TT:
    hantei += 1

for i in range(SS):
    if S[i] == T[i]:
        count += 1

if count == SS:
    hantei += 1

if hantei == 2:
    print('Yes')
else:
    print('No')
