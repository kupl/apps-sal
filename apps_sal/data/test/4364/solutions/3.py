def is_month(x):
  if 1 <= x <= 12:
    return True
  else:
    return False

S = input()
first, latter = is_month(int(S[:2])), is_month(int(S[2:]))
if first and latter:
  ans = "AMBIGUOUS"
elif not first and not latter:
  ans = "NA"
elif first:
  ans = "MMYY"
else:
  ans = "YYMM"
print(ans)
