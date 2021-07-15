s=input()
if int(s[0:2])>=1 and int(s[0:2])<=12:
    if int(s[2:4])>=1 and int(s[2:4])<=12:
        print("AMBIGUOUS")
    elif int(s[2:4])==0 or int(s[2:4])>=13:
        print("MMYY")
else:
    if int(s[2:4])>=1 and int(s[2:4])<=12:
        print("YYMM")
    else:
        print("NA")
