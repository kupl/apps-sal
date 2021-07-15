N = int(input())
ChrL = [[] for T in range(0,26)]
for NT in range(0,N):
    S = input()
    for ST in range(0,26):
        ChrL[ST].append(S.count(chr(97+ST)))
Disp = ['']*26
for ST in range(0,26):
    Disp[ST] = chr(97+ST)*min(ChrL[ST])
print(''.join(Disp))
