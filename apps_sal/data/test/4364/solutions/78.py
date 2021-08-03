S = str(input())
F = S[:2]
L = S[2:]
if F == "00" or int(F) > 12:
    if L == "00" or int(L) > 12:
        ans = "NA"
    else:
        ans = "YYMM"
elif int(F) <= 12:
    if int(L) >= 1 and int(L) <= 12:
        ans = "AMBIGUOUS"
    else:
        ans = "MMYY"
print(ans)
