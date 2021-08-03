s = str(input())
ans = "NA"
x = int(s[0:2])
y = int(s[2:4])
if x > 0 and x < 13:
    ans = "MMYY"
if y > 0 and y < 13:
    ans = "YYMM"
if x > 0 and x < 13 and y > 0 and y < 13:
    ans = "AMBIGUOUS"
print(ans)
