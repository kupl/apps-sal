# Answer
S = input()
S = int(S)
A = S // 100
B = S % 100

if 1 <= A <= 12 and 1 <= B <= 12:
    print("AMBIGUOUS")
elif (A == 0 or A > 12) and (B == 0 or B > 12):
    print("NA")
elif (A == 0 or A > 12) and 1 <= B <= 12:
    print("YYMM")
else:
    print("MMYY")
