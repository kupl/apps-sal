ov = 2**32-1
cnt = 1
x = 0
t = int(input())
st = []
for i in range(t):
	s = input().split()
	if s[0] == "for":
		if len(st) == 0:
			st.append(int(s[1]))
		else:
			if st[len(st) - 1] != -1 and st[len(st) - 1] * int(s[1]) < ov:
				st.append(st[len(st) - 1] * int(s[1]))
			else:
				st.append(-1)
	elif s[0] == "end":
		st.pop()
	else:
		if len(st) != 0 and st[len(st) - 1] == -1:
			x = 2**33
			break
		elif len(st) == 0:
			x += 1
		else:
			x += st[len(st) - 1]

if (x > ov):
	print("OVERFLOW!!!")
else:
	print(x)

