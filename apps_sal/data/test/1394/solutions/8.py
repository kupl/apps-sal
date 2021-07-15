import sys

S=input()

L=len(S)


S2=""

for s in S:
    if s!="a":
        S2+=s

if len(S2)%2!=0:
    print(":(")
    return

L2=len(S2)//2

if L2==0:
    print(S)
    return

S3=S2[:L2]

if S[-L2:]==S3:
    print(S[:-L2])
    
else:
    print(":(")
    return

    

