S = input()

if(S[0]=="R" and S[1]=="R" and S[2]=="R"):
    print(3)
elif(S[0]=="S" and S[1]=="R" and S[2]=="R"):
    print(2)
elif(S[0]=="R" and S[1]=="R" and S[2]=="S"):
    print(2)
elif(S[0]=="S" and S[1]=="S" and S[2]=="R"):
    print(1)
elif(S[0]=="S" and S[1]=="R" and S[2]=="S"):
    print(1)
elif(S[0]=="R" and S[1]=="S" and S[2]=="S"):
    print(1)
elif(S[0]=="R" and S[1]=="S" and S[2]=="R"):
    print(1)
else:
    print(0)
