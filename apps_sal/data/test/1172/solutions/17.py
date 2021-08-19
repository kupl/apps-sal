S = input()
N = len(S)
mod = 10 ** 9 + 7
numofA = 0
numofAB = 0
numofABC = 0
numofquestion = 1
for i in range(N):
    if S[i] == '?':
        numofABC = (numofABC * 3 + numofAB) % mod
        numofAB = (numofAB * 3 + numofA) % mod
        numofA = (numofquestion + numofA * 3) % mod
        numofquestion = numofquestion * 3 % mod
    elif S[i] == 'C':
        numofABC = (numofAB + numofABC) % mod
    elif S[i] == 'B':
        numofAB = (numofAB + numofA) % mod
    else:
        numofA = (numofquestion + numofA) % mod
print(numofABC)
