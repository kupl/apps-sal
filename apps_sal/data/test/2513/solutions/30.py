n=int(input())
s=list(input())
s=s+s
x=[["S","S"],["S","W"],["W","S"],["W","W"]]

for temp1 in x:
    if s[0]=="o":
        c=temp1[1]
    else:
        if temp1[1]=="S":
            c="W"
        else:
            c="S"
    for i in range(1,n+1):
        if s[i]=="o":
            if temp1[i]=="S":
                temp1.append(temp1[i-1])
                
            else:
                if temp1[i-1]=="S":
                    temp1.append("W")
                else:
                    temp1.append("S")
        else:
            if temp1[i]=="W":
                temp1.append(temp1[i-1])
            else:
                if temp1[i-1]=="W":
                    temp1.append("S")
                else:
                    temp1.append("W")
    
    
    if temp1[0]==temp1[-2] and temp1[1]==temp1[-1]:
        print("".join(temp1[:n]))
        return
print(-1)
