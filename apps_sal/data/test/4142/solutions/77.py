S = input()

Odd = ["R", "U", "D"]
Even = ["L", "U", "D"]
S_l = len(S)
result = "Yes"

for i in range(0, S_l):
    if i % 2 == 0:
        if not S[i] in Odd:
            result = "No"
            break
    if i % 2 != 0:
        if not S[i] in Even:
            result = "No"
            break

print(result)
