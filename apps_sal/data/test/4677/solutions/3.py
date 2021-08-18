S = input()
STR = ""
for i in S:
    STR = STR + i
    if i == "B" and STR == "":
        STR = ""
    elif i == "B":
        STR = STR[:len(STR) - 2]
print(STR)
