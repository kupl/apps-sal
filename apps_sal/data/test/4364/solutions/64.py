# ABC126 B

S = list(map(int, input()))
if 1 <= S[0] * 10 + S[1] <= 12 and 1 <= S[2] * 10 + S[3] <= 12:
    print("AMBIGUOUS")
elif 1 <= S[0] * 10 + S[1] <= 12 and (S[2] * 10 + S[3] > 12 or S[2] * 10 + S[3] == 0):
    print("MMYY")
elif (S[0] * 10 + S[1] > 12 or S[0] * 10 + S[1] == 0) and 1 <= S[2] * 10 + S[3] <= 12:
    print("YYMM")
elif (S[0] * 10 + S[1] > 12 or S[0] * 10 + S[1] == 0) and (S[2] * 10 + S[3] > 12 or S[2] * 10 + S[3] == 0):
    print("NA")
