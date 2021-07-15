S=input()
if S[0]=='A' and S.count('C')==1 and 'C' in S[2:-1]:
    for c in S[1:len(S)]:
        if not (c.islower() or c=='C'):
            print("WA")
            break
    else:
        print("AC")
else:
    print("WA")

