S = str(input())

if S == "AccccCcccc":
    print('AC')
    
elif S[0] == "A":
    S1 = "a"+S[1:]
    if S[2] == "C":
        S2 = S1[:2]+"c"+S1[3:]
        if S2.islower():
            print("AC")
        else:
            print("WA")

    elif S[-2] == "C":
        S2 = S1[:-2]+"c"+S1[-1]
        if S2.islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")

else:
    print("WA")

