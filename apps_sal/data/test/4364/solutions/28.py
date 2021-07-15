s = int(input())
b = s%100
a = (s - b)//100
if (0 < a <= 12 and 0 < b <= 12):
    print("AMBIGUOUS")
elif (0 < a <= 12):
    print("MMYY")
elif (0 < b <= 12):
    print("YYMM")
else:
    print("NA")

