S = str(input())
S_list = sorted(S)
if S_list[0] + S_list[1] + S_list[2] == "abc":
    print("Yes")
else:
    print("No")
