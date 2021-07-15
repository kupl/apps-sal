for nt in range(int(input())):
	n = int(input())
	s = input()
	if "1" not in s:
		print (s)
		continue
	ans = ""
	for i in range(n):
		if s[i]=="0":
			ans += s[i]
		else:
			ind = i
			break
	temp = ""
	for i in range(n-1,ind-1,-1):
		if s[i]=="0":
			ans += "0"
			break
		else:
			temp += "1"
	ans += temp
	print (ans)

