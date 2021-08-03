S = input()
MM = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

if S[:2] in MM and S[2:] in MM:
    print("AMBIGUOUS")
elif S[:2] in MM:
    print("MMYY")
elif S[2:] in MM:
    print("YYMM")
else:
    print("NA")
