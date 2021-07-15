S=input()
T=input()

dict_S={}
dict_T={}

for x, y in zip(S, T):
    if x not in dict_S:
        dict_S[x] = y
    else:
        if dict_S[x] != y:
            print("No")
            return

    if y not in dict_T:
        dict_T[y] = x
    else:
        if dict_T[y] != x:
            print("No")
            return


print("Yes")
