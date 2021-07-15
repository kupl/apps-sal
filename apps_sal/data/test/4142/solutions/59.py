S=input()
for i in range(len(S)):
    if i%2==0:
        if S[i] not in "RUD":
            print("No")
            break
    else:
        if S[i] not in "LUD":
            print("No")
            break
else:
    print("Yes")

