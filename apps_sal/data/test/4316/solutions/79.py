S = list(input())

S.sort()
# print(S)

if S[0] == S[1]:
    if S[2] == S[3]:
        if S[0] != S[2]:
            print("Yes")

        else:
            print("No")

    else:
        print("No")

else:
    print("No")
