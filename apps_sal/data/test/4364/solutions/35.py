S = list(input())
month = ["0" + str(i) for i in range(1, 10)]
month.append("10")
month.append("11")
month.append("12")

First = S[:2]
Fmonthflag = 0
if "".join(First) in month:
    Fmonthflag = 1

Latter = S[2:]
Lmonthflag = 0
if "".join(Latter) in month:
    Lmonthflag = 1

if Fmonthflag == 1 and Lmonthflag == 0:
    print("MMYY")
elif Fmonthflag == 0 and Lmonthflag == 1:
    print("YYMM")
elif Fmonthflag == 1 and Lmonthflag == 1:
    print("AMBIGUOUS")
elif Fmonthflag == 0 and Lmonthflag == 0:
    print("NA")
