s=input()
yy = ["%02d" % i for i in range(100)]
mm = ["%02d" % i for i in range(1, 13)]
yymm = s[:2] in yy and s[2:] in mm
mmyy = s[:2] in mm and s[2:] in yy
print((["NA","MMYY","YYMM","AMBIGUOUS"][yymm*2+mmyy]))

