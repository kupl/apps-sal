import string
s = string.ascii_lowercase
s += "C"
S = input()
buttanA = False
buttanB = False
buttanC = True


for i in range(len(S)):
    if S[0] == "A":
        buttanA = True
    if S[i] == "C" and 2 <= i < len(S) - 1:
        if buttanB == False:
            buttanB = True
        else:
            print("WA")
            return
    if S[i] not in s and 1 <= i < len(S):
        buttanC = False

if buttanA == buttanB == buttanC == True:
    print("AC")
else:
    print("WA")
