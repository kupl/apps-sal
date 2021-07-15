d = "AHIMOoTUVvWwXxY"
s = input()
for i in range(len(s) // 2 + 1):
	if not ((s[i] in d) and (s[i] == s[-i-1])) and not ((s[i] + s[-i-1]) in ["bd", "db", "pq", "qp"]):
		print("NIE")
		break
else:
	print("TAK")
