S = input()
C_cnt = 0
if S[0] == 'A' and S[1].islower() and S[-1].islower():
    temp = S[2:len(S)]
    if temp.count('C') == 1:
        for t in temp:
            if t != "C" and t.isupper() == True:
                print("WA")
                return
        else:
            print("AC")
            return
print("WA")
