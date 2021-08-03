S = input()
if S[len(S) - 1] == "s":
    S = S + "es"
else:
    S = S + "s"
print(S)
