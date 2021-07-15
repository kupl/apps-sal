r, c = map(int, input().split())

for i in range(r-1):
	s = input()
s = input()

x = 0
cnt = 0
for i in range(c):
	if s[i] == "B":
		x += 1
	else:
		if x > 0:
			cnt += 1
		x = 0
if x > 0:
	cnt += 1
print (cnt)
