S = input()
if S[0] == S[1] == S[2] == "R":
    print(3)
elif S[1] == S[2] =="R" or S[1] == S[0] == "R":
    print(2)
elif "R" in set(list(S)):
    print(1)
else:
    print(0)
