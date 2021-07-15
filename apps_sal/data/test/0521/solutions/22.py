cc = int(input())
dd = input()
flag=0
for i in range(1,cc):
    if dd[i]!='?' and dd[i]==dd[i-1]:
        print("No")
        flag=1
        break
if flag==0:
    if dd[0]=='?':
        print("Yes")
    elif dd[cc-1]=='?':
        print("Yes")
    else:
        count = 1
        flag =1
        for i in range(0,cc):
            if dd[i]=="?":
                if dd[i+1]=="?":
                    print("Yes")
                    flag=0
                    break
                else:
                    if dd[i-1]==dd[i+1]:
                        print("Yes")
                        flag=0
                        break
        if flag==1:
            print("No")

