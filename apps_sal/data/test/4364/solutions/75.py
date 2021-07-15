n = input()
s, t = (1 <= int(n[:2]) <= 12), (1 <= int(n[2:]) <= 12)
print("AMBIGUOUS" if s and t else "YYMM" if t else "MMYY" if s else "NA")
