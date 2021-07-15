s = input().rstrip()

a = int(s[:2])
b = int(s[2:])
if 1 <= a <= 12 and 1 <= b <= 12:
    print("AMBIGUOUS")
elif (a == 0 or 13 <= a <= 99) and 1 <= b <= 12:
    print("YYMM")
elif 1 <= a <= 12 and (b == 0 or 13 <= b <= 99):
    print("MMYY")
else:
    print("NA")
