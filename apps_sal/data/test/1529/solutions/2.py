n = int(input())
for i in range(n):
    S = input()
    flag1 = len(S) >= 5 and S[:5] == "miao."
    flag2 = len(S) >= 5 and S[-5:] == "lala."
    if flag1 and flag2:
        print("OMG>.< I don't know!")
    elif flag2:
        print("Freda's")
    elif flag1:
        print("Rainbow's")
    else:
        print("OMG>.< I don't know!")
