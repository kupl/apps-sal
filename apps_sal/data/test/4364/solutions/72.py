a = input()
b = int(a[0] + a[1])
c = int(a[2] + a[3])
if 1 <= b <= 12:
    if 1 <= c <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 1 <= c <= 12:
        print("YYMM")
    else:
        print("NA")
