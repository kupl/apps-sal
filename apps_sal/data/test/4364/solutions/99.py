s = input()
a = s[0] + s[1]
b = s[2] + s[3]
p = 0
q = 0
if a == "01" or a == "02" or a == "03" or a == "04" or a == "05" or a == "06" or a == "07" or a == "08" or a == "09" or a == "10" or a == "11" or a == "12":
    p = 1
if b == "01" or b == "02" or b == "03" or b == "04" or b == "05" or b == "06" or b == "07" or b == "08" or b == "09" or b == "10" or b == "11" or b == "12":
    q = 1  
if p == 1 and q == 1:
    print("AMBIGUOUS")
elif p == 1 and q == 0:
    print("MMYY")
elif p == 0 and q == 1:
    print("YYMM")
else:
    print("NA")
