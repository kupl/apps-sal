import sys
S = input()

if not (S[0] == "A" and "C" in S[2:len(S) - 1]):
    print("WA")
    return

S = sorted(S)

if not S[1] == "C":
    print("WA")
    return

if not "a" <= S[2] <= "z":
    print("WA")
    return

print("AC")
