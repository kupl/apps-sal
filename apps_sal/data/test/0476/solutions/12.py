I=input()
count=0
four=0
for i in I:
    if i!="1":
        if i!="4":
            print("NO")
            break
        else:
            if four==0:
                print("NO")
                break
            else:
                count+=1
                four-=1
    else:
        count+=1
        four=2
if count==len(I): print("YES")
