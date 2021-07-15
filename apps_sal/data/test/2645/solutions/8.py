S = input()
PossiblePaper = 0
Score = 0
for s in S:
    if s == "g":
        if PossiblePaper == 0:
            Score += 0
            PossiblePaper += 1
        else:
            Score += 1
            PossiblePaper -= 1
    else:
        if PossiblePaper == 0:
            Score -= 1
            PossiblePaper += 1
        else:
            Score += 0
            PossiblePaper -= 1
print(Score)

