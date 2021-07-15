n = int(input())
s = input()
p = "ogo"
while len(p) < len(s):
	p += "go"
while len(p) > 1:
	s = s.replace(p, "***")
	p = p[:-2]
print(s) 
