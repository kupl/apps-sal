A,B,C = list(map(int,input().split()))

if  A == B == C :
    print("No")
elif A == B or A == C :
    print("Yes")
elif B == C :
    print("Yes")
else :
    print("No")

