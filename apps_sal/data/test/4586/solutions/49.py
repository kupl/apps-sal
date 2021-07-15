S = input()
if len(list(set(S[:-1]))) == 1 or len(list(set(S[1:]))) == 1:
    print("Yes")
else:
    print("No")
