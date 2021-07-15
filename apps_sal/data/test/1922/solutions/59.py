n = list(map(int,input().split()))


if(n[0]==1 or n[1]==1):
    tmp = max(n)
    if(tmp == 1):
        print("1")
    elif(tmp == 2):
        print("0")
    else:
        print(tmp-2)
elif((n[0] == 2 or n[1] == 2)and(n[0]!=1 and n[1]!=1)):
    print("0")
else:
    print((n[0]-2)*(n[1]-2))
