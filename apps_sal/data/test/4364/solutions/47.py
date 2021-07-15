s = str(input())
s_ov = s[:2]
s_un = s[2:]

if int(s_ov) >= 1 and int(s_ov) <= 12:
    if int(s_un) >= 1 and int(s_un) <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
elif int(s_un) >= 1 and int(s_un) <= 12:
    print("YYMM")
else:
    print("NA")
