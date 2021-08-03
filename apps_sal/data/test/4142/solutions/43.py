S = input()


def ans141(S: str):
    judge = 0

    for i in range(0, len(S)):
        if (i + 1) % 2 == 1:
            if S[i] == "R" or S[i] == "U" or S[i] == "D":
                continue
            else:
                judge += 1
        else:
            if S[i] == "L" or S[i] == "U" or S[i] == "D":
                continue
            else:
                judge += 1
    if judge > 0:
        return "No"
    else:
        return "Yes"


print(ans141(S))
