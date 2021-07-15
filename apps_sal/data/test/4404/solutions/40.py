a,b,c=input().split("/")
if int(a) <= 2019:
    if int(b) <= 4:
        if int(c) <= 30:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")
else:
    print("TBD")
