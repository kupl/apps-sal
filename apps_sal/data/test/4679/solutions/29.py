SA = str(input()) + "f"
SB = str(input()) + "f"
SC = str(input()) + "f"
A, B, C = 1, 0, 0
i = 0
x = SA[0]

while i < len(SA + SB + SC):
    if x == "a":
        x = SA[A]
        A += 1
    elif x == "b":
        x = SB[B]
        B += 1
    elif x == "c":
        x = SC[C]
        C += 1

    if A == len(SA):
        ans = "A"
        break
    elif B == len(SB):
        ans = "B"
        break
    elif C == len(SC):
        ans = "C"
        break
    i += 1
print(ans)
