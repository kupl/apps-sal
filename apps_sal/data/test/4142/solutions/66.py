S = list(input())


def judge():
    judge = True
    for i in range(1, 1 + len(S)):
        if i % 2 == 0 and (S[i - 1] == "L" or S[i - 1] == "U" or S[i - 1] == "D"):
            continue
        elif i % 2 == 1 and (S[i - 1] == "R" or S[i - 1] == "U" or S[i - 1] == "D"):
            continue
        else:
            judge = False
            break
    if (judge):
        return "Yes"
    else:
        return "No"


print((judge()))
