s = input()

j = len(s) - 1
i = 0
while s[j] == '0' :
	j-=1
	if s[i] == '0':
		i-=1

res = True
for x in range(i,j+1):
	if s[x] != s[j-x]:
		res = False
		break

print("YES" if res else "NO")
