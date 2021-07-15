t = int(input())
for i in range(t):
    s = input()
    c = 0
    m = []
    j = 0 
    while j<(len(s)-4):
        if ((s[j]=="t") and (s[j+1]=="w") and (s[j+2]=="o") and (s[j+3]=="n") and (s[j+4]=="e") ):
            c+=1
            m.append(j+3)
            j+=5
        elif ((s[j]=="t") and (s[j+1]=="w") and (s[j+2]=="o"))or ((s[j]=="o") and (s[j+1]=="n") and (s[j+2]=="e")):
            m.append(j+2)
            c+=1
            j+=3
        else:
            j+=1
    while j<(len(s)-2):
        if ((s[j]=="t") and (s[j+1]=="w") and (s[j+2]=="o"))or ((s[j]=="o") and (s[j+1]=="n") and (s[j+2]=="e")):
            m.append(j+2)
            c+=1
            j+=3
        else:
            j+=1
    
    print(c)
    for j in m:
        print(j,end=' ')
    print()

