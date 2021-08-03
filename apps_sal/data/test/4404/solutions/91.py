a = list(input().split("/"))
month = int(a[1])
date = int(a[2])
if month < 4:
    print("Heisei")
elif month == 4 and date <= 30:
    print("Heisei")
else:
    print("TBD")
