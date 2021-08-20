s = str(input())
slen = len(s)
cmin = 998
for cnt in range(0, slen - 2, 1):
    cmin = min(cmin, abs(753 - int(s[cnt:cnt + 3])))
print(cmin)
