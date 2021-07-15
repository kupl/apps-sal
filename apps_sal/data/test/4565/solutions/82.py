N = int(input())
S = input()
 
oE = S.count("E")
Wo = 0

L = []
for i in range(N):
    if i == 0:
        if S[i] == "E":
            oE -= 1
    else:
        if S[i-1] == "W":
            Wo += 1
        if S[i] == "E":
            oE -= 1
    L.append(Wo + oE)
    if Wo + oE == 0:
        break
print(min(L))
