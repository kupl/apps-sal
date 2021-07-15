S = input()

def isKaibun(s1) :
    s2 = ""
    i = len(s1)
    
    while(i > 0) :
        i -= 1
        s2 += s1[i]
    if(s1 == s2) :
        return True
    return False

con1 = isKaibun(S)
con2 = isKaibun(S[:(len(S)-1)//2])
con3 = isKaibun(S[(len(S)+3)//2-1:])
if(con1 and con2 and con3) :
    print("Yes")
else :
    print("No")
