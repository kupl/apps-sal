s = input()
if int(s[0:4]) < 2019:
    print("Heisei")
elif int(s[0:4]) > 2019:
    print("TBD")
else:
    if int(s[5]) == 1 or int(s[6]) > 4:
        print("TBD")
    elif int(s[6]) <= 4:
        print("Heisei")
