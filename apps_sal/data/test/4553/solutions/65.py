a, b = map(int, input().split())
s = input()
t = s[:a] + s[a+1:]

if s[a]=='-' and '-' not in t:
	print("Yes")
else:
	print("No")
