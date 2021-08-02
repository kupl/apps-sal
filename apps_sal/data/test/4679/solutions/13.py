SA = input()
SB = input()
SC = input()
R = SA[0]
SA = SA[1:]
while not R == "":
    if R == "a":
        R = SA[:1]
        SA = SA[1:]
        E = "A"
    elif R == "b":
        R = SB[:1]
        SB = SB[1:]
        E = "B"
    else:
        R = SC[:1]
        SC = SC[1:]
        E = "C"
print(E)
