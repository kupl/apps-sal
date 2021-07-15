map = {0:0, 1:5, 2:3, 3:2, 4:4, 5:1}
s = "{:>06b}".format(int(input()))
s2 = [""]*6
for i in range(6):
	s2[map[i]]=s[i]
print(int("".join(s2), 2))
