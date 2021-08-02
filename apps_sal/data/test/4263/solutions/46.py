# ACGT
S = input()
ct = 0
ctM = [0]
for i in range(len(S)):
    if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
        ct += 1
        if i == len(S) - 1:
            ctM.append(ct)
    else:
        ctM.append(ct)
        ct = 0
print((max(ctM)))
