s = input()
S = sorted(s)
S.sort()
flag = False
if S[0] == S[1]:
    if S[2] == S[3]:
        if S[1] != S[2]:
            flag = True
if flag:
    print("Yes")
else:
    print("No")
