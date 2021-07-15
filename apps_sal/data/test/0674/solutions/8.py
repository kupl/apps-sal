L = {}
R = {}
S = set()

for _ in range(int(input())):
    s = input()
    if len(s) == 1: 
        S.add(s)
    for s1, s2 in zip(s, s[1:]):
        if  s2 != L.get(s1, s2) or s1 != R.get(s2, s1): 
            print('NO');return
        L[s1], R[s2] = s2, s1

L1, R1 = set(L), set(R)
S = S -L1 - R1

for i in L1 - R1:
    while i[-1] in L: 
        i += L.pop(i[-1])
    S.add(i)
if L: 
    print('NO');return
print(''.join(sorted(S)))
