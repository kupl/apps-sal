s = input()
x = int(s[:2])
y = int(s[2:])
if 1 <= x <= 12 and 1 <= y <= 12:
    a = "AMBIGUOUS"
elif 1 <= x <= 12:
    a = "MMYY"
elif 1 <= y <= 12:
    a = "YYMM"
else:
    a = "NA"
print(a)
