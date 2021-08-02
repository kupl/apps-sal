S = input()
s1 = S[0:2]
s2 = S[2:4]
li = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

if s1 not in li:
    a = False
else:
    a = True
if s2 not in li:
    b = False
else:
    b = True

if a == b == True:
    print("AMBIGUOUS")
elif a == b == False:
    print("NA")
elif a == True:
    print("MMYY")
else:
    print("YYMM")
