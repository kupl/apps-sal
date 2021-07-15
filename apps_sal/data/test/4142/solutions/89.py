S = input()
for i in range(1,len(S)+1):
    if(i % 2 == 1):
        if(S[i-1] == "R" or S[i-1] == "U" or S[i-1] == "D"):
            continue
        else:
            print("No")
            return
    else:
        if(S[i-1] == "L" or S[i-1] == "U" or S[i-1] == "D"):
            continue
        else:
            print("No")
            return
print("Yes")
