inp = input().strip()

if len(inp) < 4:
	print("NO")
else:
	if inp.count("AB") == 1 and inp.count("BA") == 1:
		if inp.count("ABA") + inp.count("BAB") >= 1:
			print("NO")
		else:
			print("YES")
	elif inp.count("AB") < 1 or inp.count("BA") < 1:
		print("NO")
	elif inp.count("AB") + inp.count("BA") == 3 and inp.count("ABAB") + inp.count("BABA") >= 1:
		print("NO")
	else:
		print("YES")
