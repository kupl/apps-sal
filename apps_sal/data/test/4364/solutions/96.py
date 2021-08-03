def YY(x):
    if 1 <= x and x <= 12:
        return True
    else:
        return False


S = input()
A = int(S[0:2])
B = int(S[2:4])
if YY(A) and YY(B):
    print("AMBIGUOUS")
elif YY(A):
    print("MMYY")
elif YY(B):
    print("YYMM")
else:
    print("NA")
