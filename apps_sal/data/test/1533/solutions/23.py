t = int(input())
s = set()
while(t):
	t -= 1
	temp = input().strip()
	if temp in s:
		print("YES")
	else:
		print("NO")
	s.add(temp)
