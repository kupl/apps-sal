S = input()
S_list = list(S)
if S[0] != S[1] and S[1] != S[2]:
    print(1)
else:
    print(S_list.count("R"))
